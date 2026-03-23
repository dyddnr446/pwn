	.file	"test.c"
	.intel_syntax noprefix
	.text
	.globl	callee
	.type	callee, @function
callee:
	push	ebp
	mov	ebp, esp
	mov	edx, DWORD PTR [ebp+8]
	mov	eax, DWORD PTR [ebp+12]
	add	edx, eax
	mov	eax, DWORD PTR [ebp+16]
	add	eax, edx
	pop	ebp
	ret	12
	.size	callee, .-callee
	.globl	_start
	.type	_start, @function
_start:
	push	ebp
	mov	ebp, esp
	push	3
	push	2
	push	1
	call	callee
	nop
	leave
	ret
	.size	_start, .-_start
	.ident	"GCC: (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0"
	.section	.note.GNU-stack,"",@progbits
