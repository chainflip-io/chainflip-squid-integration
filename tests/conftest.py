import pytest
from brownie.network import priority_fee
from params import *

# Test isolation
@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass


# Deploy the contracts for repeated tests without having to redeploy each time
@pytest.fixture(scope="module")
def cf(a, Vault, CFReceiver, Token):
    priority_fee("1 gwei")

    cf.deployer = a[0]
    cf.ALICE = a[1]
    cf.BOB = a[2]
    cf.CHARLIE = a[3]
    cf.DENICE = a[4]

    cf.vault = cf.deployer.deploy(Vault, cf.ALICE, cf.BOB, cf.CHARLIE)
    cf.cfReceiver = cf.deployer.deploy(CFReceiver, cf.vault.address)
    cf.token = cf.deployer.deploy(Token)
    cf.cfReceiver = cf.deployer.deploy(CFReceiver, cf.vault.address)

    # For example encode a token transfer for the egress chain to decode
    cf.message = cf.token.transfer.encode_input(evm_dstAddress, amountOutputSwap)
    cf.nonevm_dstAddress = cf.vault.encode_string(nonevm_dstAddress)

    # Fund the vault for the destination chain to tests
    cf.token.transfer(cf.vault, amountOutputSwap, {"from": cf.deployer})
    cf.deployer.transfer(cf.vault, amountOutputSwap)

    return cf
