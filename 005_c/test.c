// Name: cdecl.c
// Compile: gcc -fno-asynchronous-unwind-tables -nostdlib -masm=intel \
//          -fomit-frame-pointer cdecl.c -w -m32 -fno-pic -O0

void __attribute__((cdecl)) callee(int a1, int a2, int a3){ // cdecl로 호출
}

void caller(){
   callee(1, 2, 3);
}


// // __attribute__((stdcall))을 사용하여 규약을 명시합니다.
// int __attribute__((stdcall)) callee(int a, int b, int c) {
//     return a + b + c;
// }

// void _start() {
//     callee(1, 2, 3);
// }