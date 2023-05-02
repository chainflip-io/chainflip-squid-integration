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
