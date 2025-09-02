from build.ab import simplerule
from tools.build import mkcpmfs
from build.llvm import llvmrawprogram
from build.zip import zip
from config import (
    MINIMAL_APPS,
    MINIMAL_APPS_SRCS,
    BIG_APPS,
    BIG_APPS_SRCS,
    PASCAL_APPS,
    SERIAL_APPS,
    FORTH_APPS,
)

llvmrawprogram(
    name="sym-1",
    srcs=["./sym-1.S"],
    deps=["include", "src/lib+bioslib"],
    linkscript="./sym-1.ld",
)

mkcpmfs(
    name="cpmfs",
    format="generic-1m-bootable",
    items={
        "0:ccp.sys@sr": "src+ccp",
        "0:bdos.sys@sr": "src/bdos"
    }
    | MINIMAL_APPS
    | MINIMAL_APPS_SRCS
    | BIG_APPS
    | BIG_APPS_SRCS
    | PASCAL_APPS
    | SERIAL_APPS
    | FORTH_APPS,
)

simplerule(
    name="cpmfs_bootable",
    ins=[".+cpmfs", "./boot+boot.bin"],
    outs=["=cf_diskimage.img"],
    commands=[
        "cp $[ins[0]] $[outs[0]]",
        "dd if=$[ins[1]] of=$[outs[0]] bs=512 count=1 seek=0"
        
#        "cat $[ins[0]] /dev/zero | dd bs=512 count=1 > $[outs[0]]",
#        "cat $[ins[1]] >> $[outs[0]]",
    ],
    label="MAKESYM",
)

zip(
    name="images",
    items={
        "bdos.bin": "src/bdos",
        "cpm.bin": ".+sym-1",
        "boot.bin": "./boot+boot.bin",
        "sym_cf_diskimage.img": ".+cpmfs_bootable",
    },
)
