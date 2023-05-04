from params import *


# These are the calls on the source chain being sent to the destination chain.

# Using a mock SigData since we don't require signature verification for these examples.
# Any arbitrary sender can submit a signed transaction.
def signed_call_cf(fcn, *args):
    sigData = [0, 0, ZERO_ADDR]

    return fcn(
        sigData,
        *args,
    )


def test_example_executexSwapAndCallNative(cf):
    # Mimicking a call coming from an EVM-compatible chain
    srcAddress = cf.vault.encode_address(cf.deployer.address)

    iniBals_receiver = cf.cfReceiver.balance()

    # xSwapNative
    args = [
        [NATIVE_ADDR, cf.cfReceiver.address, amountOutputSwap],
        srcChain,
        srcAddress,
        cf.message,
    ]
    tx = signed_call_cf(cf.vault.executexSwapAndCall, *args)

    assert tx.events["ReceivedxSwapAndCall"][0].values() == [
        srcChain,
        srcAddress,
        cf.message,
        NATIVE_ADDR,
        amountOutputSwap,
    ]

    assert cf.cfReceiver.balance() == iniBals_receiver + amountOutputSwap


def test_example_executexSwapAndCallToken(cf):
    # Mimicking a call coming from an EVM-compatible chain
    srcAddress = cf.vault.encode_address(cf.deployer.address)

    iniBals_receiver = cf.token.balanceOf(cf.cfReceiver.address)

    # xSwapNative
    args = [
        [cf.token.address, cf.cfReceiver.address, amountOutputSwap],
        srcChain,
        srcAddress,
        cf.message,
    ]
    tx = signed_call_cf(cf.vault.executexSwapAndCall, *args)

    assert tx.events["ReceivedxSwapAndCall"][0].values() == [
        srcChain,
        srcAddress,
        cf.message,
        cf.token.address,
        amountOutputSwap,
    ]

    assert (
        cf.token.balanceOf(cf.cfReceiver.address) == iniBals_receiver + amountOutputSwap
    )
    # No native tokens have been received
    assert cf.cfReceiver.balance() == 0

# Same idea applies to pure cross-chain messaging calls without a token (cfReceivexCall).