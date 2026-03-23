from pwn import *

context.arch="amd64"
macnin_code = asm("mov eax, 0")
print(macnin_code)
assem_code = disasm(macnin_code)
print(assem_code)