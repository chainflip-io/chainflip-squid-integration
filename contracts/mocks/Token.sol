pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/**
 * @title    Token
 * @dev      Creates a standard ERC20 just for the purposes of testing
 */
contract Token is ERC20 {
    constructor() ERC20("TEST", "TST") {
        _mint(msg.sender, 1000 * 10 ** decimals());
    }
}
