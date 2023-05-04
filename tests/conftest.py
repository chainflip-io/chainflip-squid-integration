import pytest
from brownie.network import priority_fee

# Test isolation
@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass


# Deploy the contracts for repeated tests without having to redeploy each time
@pytest.fixture(scope="module")
def cf(a, Vault, CFReceiverMock, Token):
    priority_fee("1 gwei")

    cf.deployer = a[0]
    cf.ALICE = a[1]
    cf.BOB = a[2]
    cf.CHARLIE = a[3]
    cf.DENICE = a[4]

    cf.vault = cf.deployer.deploy(Vault, cf.ALICE, cf.BOB, cf.CHARLIE)
    cf.cfReceiver = cf.deployer.deploy(CFReceiverMock, cf.vault.address)
    cf.token = cf.deployer.deploy(Token)

    return cf


@pytest.fixture(scope="module")
def example_parameters(cf):
    dstChain = 0
    dstToken = 1
    dstAddress = str(cf.DENICE)
    amountToSwap = 1000

    # For example encode a token transfer for the egress chain to decode
    message = cf.token.transfer.encode_input(cf.BOB, amountToSwap)

    # Arbitrary gas amount for the egress chain to use - CF SDK will help with this
    gasAmount = amountToSwap / 100
    refundAddress = str(cf.deployer)

    # Return all parameters
    return (
        dstChain,
        dstToken,
        dstAddress,
        amountToSwap,
        message,
        gasAmount,
        refundAddress,
    )
