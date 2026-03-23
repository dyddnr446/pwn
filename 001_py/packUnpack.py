from pwn import *

# # packing은 p8,16*, unpacking은 u8,u16
# s8 = 0x41
# s16 = 0x4142
# s32 = 0x41424344
# s64 = 0x4142434445647486

# print(p8(s8))
# print(p16(s16))
# print(p32(s32))
# print(p64(s64))

A = p64(0x30313233)
B = u32(b"ABCD")

print(A)
print(B)