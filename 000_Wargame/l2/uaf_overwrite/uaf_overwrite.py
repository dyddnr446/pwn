from pwn import *

p = remote("host3.dreamhack.games",8341)
e = ELF("./libc-2.27.so")

print_elf = e.symbols["printf"]

# # 로봇의 함수 실행 값인 print를 힙에 넣어두기
# p.sendlineafter(b"> ",b'2')
# p.sendlineafter(b"Robot Weight: ",b'10')




# # printf("1. Human\n");
# #   printf("2. Robot\n");
# #   printf("3. Custom\n");
# #   printf("> ");

# # void human_func() {
# #   int sel;
# #   human = (struct Human *)malloc(sizeof(struct Human));

# #   strcpy(human->name, "Human");
# #   printf("Human Weight: ");
# #   scanf("%d", &human->weight);

# #   printf("Human Age: ");
# #   scanf("%ld", &human->age);

# #   free(human);
# # }