; CP/M-65 bootblock for the SYM-1 compact flash interface

; entry points
intchr	= $8A58		; A = Input from terminal
outchr	= $8A47		; Output to terminal = A

.section .zp, "zax", @nobits

pntr:
	.fill 2         ; General purpose pointer

.text

.global _start
_start:
	cld
    
	; post the "hello message"
	ldx	#0
1:	lda	str_hello,x
	beq	2f
	jsr	outchr
	inx
	jmp	1b
2:	jmp	2b
    
str_hello:
	.ascii	"SYM-1 CPM/65 BOOTSTRAP"
	.byte	$0A,$0D,$00