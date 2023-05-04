# NOTES:
#    - `dstAddress` and `dstToken will be values defined and provided by the Chainflip protocol.
#    - Brownie automatically converts the `dstAddress` string into bytes. In Solidity it can be done via
#           abi.encode() for example. Bytes is used to encompass all non-EVM addresses in all formats.
#    - `gasAmount in `xCallNative` and `xCallToken` will be able to be estimated via the SDK.


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
