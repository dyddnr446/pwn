	.file	"test.c"
	.intel_syntax noprefix
	.text
	.globl	callee
	.type	callee, @function
callee:
	push	ebp
	mov	ebp, esp
	nop
	pop	ebp
	ret
	.size	callee, .-callee
	.globl	caller
	.type	caller, @function
caller:
	push	ebp
	mov	ebp, esp
	push	3
	push	2
	push	1
	call	callee
	add	esp, 12
	nop
	leave
	ret
	.size	caller, .-caller
	.ident	"GCC: (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0"
	.section	.note.GNU-stack,"",@progbits
