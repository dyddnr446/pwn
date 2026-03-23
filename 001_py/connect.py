from pwn import *

# process는 내부 프로그램
p = process(["./example","AAAA"],env={"LD_PRELOAD":"./libc.so.6"})
# remote는 외부 서버에 통신
r = remote("example.com",1337,typ='tcp')
# ssh 통신 기반
s = ssh("yonguk","127.0.0.1",22,password="dreamhack")


#최대 1024 바이트로 수신
data = p.recv(1024)
#개행 문자를 만날 때 까지 받아서 저장
data = p.recvline()
#p가 출력하는 데이터를 5 바이트만 받아서 data에 저장
data = p.recvn(5)
#p가 b'hello'를 입력할 때 까지 수신하여 저장
data = p.recvuntil(b'hello')
#p가 출력하는 데이터를 프로세스가 종료될 때 까지 받아서 저장
data = p.recvall()


#./example에 바이너리 A값을 입력
p.send(b'A')
#./examle에 바이너리 A + b'\n' 값을 입력
p.sendline(b'A')
#./example이 b'hello'를 출력하면 b'A'를 입력
p.sendafter(b'hello',b'A')
#hello 값이 오면 'A'+'\n' 입력
p.sendlineafter(b'hello',b'A')

#동적으로 입력/출력
p.interactive()

#연결 닫기
p.close()

context.log_level='debug'



# gdb에 프로세스를 붙여 줌
gdb.attach()