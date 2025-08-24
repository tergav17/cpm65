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
    format="generic-1m",
    items={"0:ccp.sys@sr": "src+ccp"}
    | MINIMAL_APPS
    | MINIMAL_APPS_SRCS
    | BIG_APPS
    | BIG_APPS_SRCS
    | PASCAL_APPS
    | SERIAL_APPS
    | FORTH_APPS,
)

zip(
    name="diskimage",
    items={
        "bdos.bin": "src/bdos",
        "cpm.bin": ".+sym-1",
        "boot.bin": "src/arch/sym-1/boot+boot.bin",
        "sym_1_bootable.img": ".+cpmfs",
    },
)
