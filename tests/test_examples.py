# NOTES:
#    - `dstAddress` and `dstToken will be values defined and provided by the Chainflip protocol.
#    - Brownie automatically converts the `dstAddress` string into bytes. In Solidity it can be done via
#           abi.encode() for example. Bytes is used to encompass all non-EVM addresses in all formats.
#    - `gasAmount in `xCallNative` and `xCallToken` will be able to be estimated via the SDK.


def test_example_xSwap(cf):
    dstChain = 0
    dstToken = 1
    dstAddress = str(cf.DENICE)
    amountToSwap = 1000

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


def test_example_xCall(cf):

    dstChain = 0
    dstToken = 1
    dstAddress = str(cf.DENICE)
    amountToSwap = 1000

    # For example encode a token transfer for the egress chain to decode
    message = cf.token.transfer.encode_input(cf.BOB, amountToSwap)

    # Arbitrary gas amount for the egress chain to use - CF SDK will help with this
    gasAmount = amountToSwap / 100
    refundAddress = str(cf.deployer)

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
