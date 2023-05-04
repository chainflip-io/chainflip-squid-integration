NATIVE_ADDR = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
ZERO_ADDR = "0x0000000000000000000000000000000000000000"

# Arbitrary values defined by Chainflip
dstChain = 0
dstToken = 1
srcChain = 1

# Address on the destination chain. This shall be of types bytes.
# This doesn't need to be evm compatible.
nonevm_dstAddress = "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"
evm_dstAddress = "0xDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEF"
# Examplifying a 1:2 swap ratio
amountToSwap = 1000
amountOutputSwap = 2000

# Arbitrary gas amount for the egress chain to use - CF SDK will help with this
gasAmount = amountToSwap / 100

# Unused input for now
cfParameters = "0x0"
