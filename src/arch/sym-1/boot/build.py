from build.llvm import llvmrawprogram

llvmrawprogram(
    name="boot.bin",
    srcs=["./boot.S"],
    linkscript="./boot.ld",
)