from pwn import *

e = ELF("./example")
print(hex(e.symbols['write']))
print(hex(e.symbols.write))