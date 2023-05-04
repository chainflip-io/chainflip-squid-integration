pragma solidity ^0.8.0;

import "./interfaces/ICFReceiver.sol";

/**
 * @title    CFReceiver Example
 * @dev      This abstract contract is the base implementation for a smart contract
 *           capable of receiving cross-chain swaps and calls from the Chainflip Protocol.
 *           It has a check to ensure that the functions can only be called by one
 *           address, which should be the Chainflip Protocol. This way it is ensured that
 *           the receiver will be sent the amount of tokens passed as parameters and
 *           that the cross-chain call originates from the srcChain and address specified.
 *           Remember that anyone on the source chain can use the Chainflip Protocol
 *           to make a cross-chain call to this contract. If that is not desired, an extra
 *           check on the source address and source chain should be performed.
 */

contract CFReceiver is ICFReceiver {
    event ReceivedxSwapAndCall(
        uint32 srcChain,
        bytes srcAddress,
        bytes message,
        address token,
        uint256 amount
    );

    event ReceivedxCall(uint32 srcChain, bytes srcAddress, bytes message);

    /// @dev The address used to indicate whether the funds received are native or a token
    address private constant _NATIVE_ADDR =
        0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE;

    /// @dev    Chainflip's Vault address where _cfReceive and _cfReceivexCall will originate from
    address public cfVault;
    address public owner;

    constructor(address _cfVault) {
        cfVault = _cfVault;
        owner = msg.sender;
    }

    //////////////////////////////////////////////////////////////
    //                                                          //
    //                   CF Vault calls                         //
    //                                                          //
    //////////////////////////////////////////////////////////////

    /**
     * @notice  Receiver of a cross-chain swap and call made by the Chainflip Protocol.

     * @param srcChain      The source chain according to the Chainflip Protocol's nomenclature.
     * @param srcAddress    Bytes containing the source address on the source chain.
     * @param message       The message sent on the source chain. This is a general purpose message.
     * @param token         Address of the token received. _NATIVE_ADDR if native.
     * @param amount        Amount of tokens received. This will match msg.value for native tokens.
     */
    function cfReceive(
        uint32 srcChain,
        bytes calldata srcAddress,
        bytes calldata message,
        address token,
        uint256 amount
    ) external payable override onlyCfVault {
        // Writing assertions here just to make a statement
        if (token == _NATIVE_ADDR) {
            assert(msg.value == amount);
        } else {
            // Asserting here just to highlight this
            assert(msg.value == 0);
        }
        emit ReceivedxSwapAndCall(srcChain, srcAddress, message, token, amount);
    }

    /**
     * @notice  Receiver of a cross-chain call made by the Chainflip Protocol.

     * @param srcChain      The source chain according to the Chainflip Protocol's nomenclature.
     * @param srcAddress    Bytes containing the source address on the source chain.
     * @param message       The message sent on the source chain. This is a general purpose message.
     */
    function cfReceivexCall(
        uint32 srcChain,
        bytes calldata srcAddress,
        bytes calldata message
    ) external override onlyCfVault {
        emit ReceivedxCall(srcChain, srcAddress, message);
    }

    //////////////////////////////////////////////////////////////
    //                                                          //
    //                 Update Vault address                     //
    //                                                          //
    //////////////////////////////////////////////////////////////

    /**
     * @notice           Update Chanflip's Vault address.
     * @param _cfVault    New Chainflip's Vault address.
     */
    function updateCfVault(address _cfVault) external onlyOwner {
        cfVault = _cfVault;
    }

    //////////////////////////////////////////////////////////////
    //                                                          //
    //                          Modifiers                       //
    //                                                          //
    //////////////////////////////////////////////////////////////

    /// @dev Check that the sender is the Chainflip's Vault.
    modifier onlyCfVault() {
        require(
            msg.sender == cfVault,
            "CFReceiver: caller not Chainflip sender"
        );
        _;
    }

    /// @dev Check that the sender is the owner.
    modifier onlyOwner() {
        require(msg.sender == owner, "CFReceiver: caller not owner");
        _;
    }
}
