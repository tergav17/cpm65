; CP/M-65 bootblock for the SYM-1 compact flash interface


.section .zp, "zax", @nobits

; scrtch: .fill 9         ; Scratch RAM, Result phase readouts from NEC-765

.text

.global _start
_start:
    cld