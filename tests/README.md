# Swap examples clarifications :squid:

An description of the required parameters for the function calls is already in the code and the tests show examples of how to start cross-chain swaps and how to recieve them on the destination chain.

I am adding here are some extra clarifications for those interfaces in case you have some doubts:

- `dstChain` & `dstToken` => Destination chain and destination token will be values defined and provided by Chainflip. Each token and each chain will have an arbitrary value.
- `dstAddress` => `bytes` type is uesed to easily support any non-EVM chain regardless of their characteristics. In the examples Brownie automatically converts the `dstAddress` string into bytes. In Solidity it can be done via abi.encode() for example.
- `message` => It must be abi encoded.
- `gasAmount` in `xCallNative` and `xCallToken` => This is the amount that should be used to pay for gas on the destination chain. This will be able to be estimated via Chainflip's SDK.
- `cfParameters` => It will be used for future functionality in the protocol. For now this is not used and shall be set to zero.
- As you can see, there is no check in any of the calls for valid supported tokens nor chains. That check is done in the witnessing side of the Chainflip's protocol. This is basically to decrease the on-chain overhead of each swaps.

// TODO: Add clarifications on the receiver side.
