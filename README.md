# Chainflip - Squid integration contracts

This repository contains the Ethereum smart contracts which are used to handle deposits and withdrawals based on signatures submitted via the vault nodes.

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

We use solhint and prettier for the solidity code and black for the python code. A general check is performed also in CI.

To locally do a general check on both solidity and python code: (please ensure you have poetry installed)

```bash
yarn lint
```

Format the solidity and python code:

```bash
yarn format
```

To format them separately run `yarn format-sol` or `yarn format-py`