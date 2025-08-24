MEMORY {
    zp : ORIGIN = 0x00, LENGTH = 0xef
	ram (rw) : ORIGIN = 0x200, LENGTH = 0x0200
}

SECTIONS {
	.zp : {
		*(.zp .zp.*)
	} >zp

	.text : {
		*(.text .text.*)
	} >ram

	.init : {
		*(.init .init.*)
	} >ram

}

OUTPUT_FORMAT {
	TRIM(ram)
}

