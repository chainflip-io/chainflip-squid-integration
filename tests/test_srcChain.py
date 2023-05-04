from params import *

# An EVM address should be used when swapping to an EVM chain (e.g. evm_dstAddress)
# An abi.encoded address should be used when swapping to a non-EVM compatible
# chain (e.g. nonevm_dstAddress). Here we are showcasing both arbitrarily.

# Initiate a cross-chain swap of a native token (provided by the user/Squid)
# without cross-chain messaging.
def test_example_xSwapNative(cf):
    # xSwapNative
    tx = cf.vault.xSwapNative(
        dstChain,
        evm_dstAddress,
        dstToken,
        cfParameters,
        {"value": amountToSwap, "from": cf.deployer},
    )

    assert tx.events["SwapNative"][0].values() == [
        dstChain,
        evm_dstAddress,
        dstToken,
        amountToSwap,
        cf.deployer,
        cfParameters,
    ]


# Initiate a cross-chain swap of Chainflip supported ERC20 token (provided by the
# user/Squid) without cross-chain messaging.
def test_example_xSwapToken(cf):

    # xSwapToken
    cf.token.approve(cf.vault, amountToSwap, {"from": cf.deployer})
    tx = cf.vault.xSwapToken(
        dstChain,
        cf.nonevm_dstAddress,
        dstToken,
        cf.token.address,
        amountToSwap,
        cfParameters,
        {"from": cf.deployer},
    )

    assert tx.events["SwapToken"][0].values() == [
        dstChain,
        cf.nonevm_dstAddress,
        dstToken,
        cf.token.address,
        amountToSwap,
        cf.deployer,
        cfParameters,
    ]


# Initiate a cross-chain swap of a native token (provided by the user/Squid)
# with cross-chain messaging triggering a call on the destination chain.
def test_example_xCallNative(cf):
    tx = cf.vault.xCallNative(
        dstChain,
        cf.nonevm_dstAddress,
        dstToken,
        cf.message,
        gasAmount,
        cfParameters,
        {"value": amountToSwap, "from": cf.deployer},
    )
    assert tx.events["XCallNative"][0].values() == [
        dstChain,
        cf.nonevm_dstAddress,
        dstToken,
        amountToSwap,
        cf.deployer,
        cf.message,
        gasAmount,
        cfParameters,
    ]


# Initiate a cross-chain swap of a chainflip supporoted ERC-20 token
# (provided by the user/Squid) with cross-chain messaging triggering
# a call on the destination chain.
def test_example_xCallToken(cf):
    cf.token.approve(cf.vault, amountToSwap, {"from": cf.deployer})
    tx = cf.vault.xCallToken(
        dstChain,
        evm_dstAddress,
        dstToken,
        cf.message,
        gasAmount,
        cf.token.address,
        amountToSwap,
        cfParameters,
        {"from": cf.deployer},
    )
    assert tx.events["XCallToken"][0].values() == [
        dstChain,
        evm_dstAddress,
        dstToken,
        cf.token.address,
        amountToSwap,
        cf.deployer,
        cf.message,
        gasAmount,
        cfParameters,
    ]
