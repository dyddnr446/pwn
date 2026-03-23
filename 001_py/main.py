from pwn import *

context.log_level="debug"

r = remote("host8.dreamhack.games",9486)

r.recvuntil(b"There are 50 rounds.\n")

for n in range(50):
    r.recvline()
    response = 0
    for i in range(10):
        if b"flag" in r.recvline():
            response = i
            break
    r.sendlineafter(b"> ", str(response).encode())

r.interactive()