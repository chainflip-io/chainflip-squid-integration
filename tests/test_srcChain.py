# Initiate a cross-chain swap of a native token (provided by the user/Squid) 
# without cross-chain messaging.
def test_example_xSwapNative(cf, example_parameters):
    dstChain, dstToken, dstAddress, amountToSwap, _, _, _ = example_parameters
    # xSwapNative
    tx = cf.vault.xSwapNative(
        dstChain, dstAddress, dstToken, {"value": amountToSwap, "from": cf.deployer}
    )

    assert tx.events["SwapNative"][0].values() == [
        dstChain,
        dstAddress,
        dstToken,
        amountToSwap,
        cf.deployer,
    ]

# Initiate a cross-chain swap of Chainflip supported ERC20 token (provided by the 
# user/Squid) without cross-chain messaging.
def test_example_xSwapToken(cf, example_parameters):
    dstChain, dstToken, dstAddress, amountToSwap, _, _, _ = example_parameters

    # xSwapToken
    cf.token.approve(cf.vault, amountToSwap, {"from": cf.deployer})
    tx = cf.vault.xSwapToken(
        dstChain,
        dstAddress,
        dstToken,
        cf.token.address,
        amountToSwap,
        {"from": cf.deployer},
    )

    assert tx.events["SwapToken"][0].values() == [
        dstChain,
        dstAddress,
        dstToken,
        cf.token.address,
        amountToSwap,
        cf.deployer,
    ]

# Initiate a cross-chain swap of a native token (provided by the user/Squid) 
# with cross-chain messaging triggering a call on the destination chain.
def test_example_xCallNative(cf, example_parameters):

    (
        dstChain,
        dstToken,
        dstAddress,
        amountToSwap,
        message,
        gasAmount,
        refundAddress,
    ) = example_parameters

    tx = cf.vault.xCallNative(
        dstChain,
        dstAddress,
        dstToken,
        message,
        gasAmount,
        refundAddress,
        {"value": amountToSwap, "from": cf.deployer},
    )
    assert tx.events["XCallNative"][0].values() == [
        dstChain,
        dstAddress,
        dstToken,
        amountToSwap,
        cf.deployer,
        message,
        gasAmount,
        refundAddress,
    ]

# Initiate a cross-chain swap of a chainflip supporoted ERC-20 token 
# (provided by the user/Squid) with cross-chain messaging triggering 
# a call on the destination chain.
def test_example_xCallToken(cf, example_parameters):
    (
        dstChain,
        dstToken,
        dstAddress,
        amountToSwap,
        message,
        gasAmount,
        refundAddress,
    ) = example_parameters

    cf.token.approve(cf.vault, amountToSwap, {"from": cf.deployer})
    tx = cf.vault.xCallToken(
        dstChain,
        dstAddress,
        dstToken,
        message,
        gasAmount,
        cf.token.address,
        amountToSwap,
        refundAddress,
        {"from": cf.deployer},
    )
    assert tx.events["XCallToken"][0].values() == [
        dstChain,
        dstAddress,
        dstToken,
        cf.token.address,
        amountToSwap,
        cf.deployer,
        message,
        gasAmount,
        refundAddress,
    ]


# TODO: CFReceieve Mock tests
