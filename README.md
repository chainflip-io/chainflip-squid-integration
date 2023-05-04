# :squid: Chainflip - Squid integration :squid:

This repository contains the Vault smart contract which is used to handle deposits and withdrawals based on signatures submitted via the vault nodes.

There is a couple of simplifications in the Vault (added as notes in the code) because we have a KeyManager contract that holds addresses and keys and performs signature verification. That requires a bunch of dependencies. Instead, I have just added the addresses to the Vault and commented out the signature verification call. This way the repository is greatly simplified.

These are the relevant functions for the integration with Squid:
- `xSwapNative` - Start a cross-chain swap providing the native token with no message passing.
- `xSwapToken`  - Start a cross-chain swap providing an ERC20 token with no message passing.
- `xCallNative` - Start a cross-chain swap providing the native token with message passing.
- `xCallToken`  - Start a cross-chain swap providing an ERC20 token with message passing.

- `executexSwapAndCall` - Egressing native swap tokens with a message. The `cfReceive` interface is expected.
- `executexCall` - General message passing egress without token. The `cfReceivexCall` interface is expected.

Althought most of those function calls are straightforward, you will find an example of each of them under the tests directory. You will also find another README file with some clarifications under that same directory.

When it comes to the integration, my understanding is that there are several points of integration.

- Squid adding support for `cfReceive`  to receive the egress calls with tokens from Chainflip. This is analogous to Axelar's `executeWithToken`. I am not sure if you also aim to support pure general message passing via `cfReceivexCall`
as I don't seem to see Axelar's `execute` being implemented. Anyway, the expected interface is defined in `ICFReceiver.sol`, a baseline for an example contract is `CFReceiver.sol`, which is used as a receiver in the tests.

- Integrating the calls `xSwapNative`, `xSwapToken`,`xCallNative`,`xCallToken` to be able to initiate swaps through the Chainflip Vault. There are two options that come to my mind:

    **A)** Integrate Chainflip at the same level as Axelar, as in `_bridgeCall()` (aka hardcoded calls in the contract).

    **B)** On our call you mentioned that another option is just integrating on the backend and use `fundAndRunMulticall()` to do the call to Chainflip. As we discussed, it would be interesting to do gas comparisons between those two options in order to figure out what is best. This estimations could be done right now just by calling axelar via `bridgeCall()` or `fundAndRunMulticall()`. It should be cheaper via the former but I'm not sure how much cheaper.



## Dependencies

- Python 2.7 or 3.5+
  For Ubuntu `sudo apt-get install python3 python-dev python3-dev build-essential`
- [Poetry (Python dependency manager)](https://python-poetry.org/docs/)

## Setup

First, ensure you have [Poetry](https://python-poetry.org), [Yarn](https://yarnpkg.com) and Ganache (`npm install -g ganache-cli`) are installed.

```bash
git clone git@github.com:chainflip-io/chainflip-squid-integration.git
cd chainflip-squid-integration
yarn
poetry shell
poetry install
brownie pm install OpenZeppelin/openzeppelin-contracts@4.0.0
```

### Linter

To locally do a general check on both solidity and python code: (please ensure you have poetry installed)

```bash
yarn lint
```

Format the solidity and python code:

```bash
yarn format
```