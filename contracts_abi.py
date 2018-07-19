home_bridge_abi = """
[
	{
		"constant": false,
		"inputs": [
			{
				"name": "_owner",
				"type": "address"
			},
			{
				"name": "_tokenVIN",
				"type": "string"
			},
			{
				"name": "_serializedData",
				"type": "bytes"
			},
			{
				"name": "_txHash",
				"type": "bytes32"
			}
		],
		"name": "transferApproved",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_from",
				"type": "address"
			},
			{
				"name": "_owner",
				"type": "address"
			},
			{
				"name": "_tokenVIN",
				"type": "string"
			},
			{
				"name": "_data",
				"type": "bytes"
			}
		],
		"name": "onERC721Received",
		"outputs": [
			{
				"name": "",
				"type": "bytes4"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"name": "_contract",
				"type": "address"
			},
			{
				"name": "_requiredSignatures",
				"type": "uint256"
			},
			{
				"name": "_authorities",
				"type": "address[]"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_from",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "_tokenVIN",
				"type": "string"
			},
			{
				"indexed": false,
				"name": "_data",
				"type": "bytes"
			}
		],
		"name": "UserRequestForSignature",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_tokenVIN",
				"type": "string"
			}
		],
		"name": "TransferCompleted",
		"type": "event"
	}
]
"""

foreign_bridge_abi = """
[
	{
		"constant": false,
		"inputs": [
			{
				"name": "_owner",
				"type": "address"
			},
			{
				"name": "_tokenVIN",
				"type": "string"
			},
			{
				"name": "_serializedData",
				"type": "bytes"
			},
			{
				"name": "_txHash",
				"type": "bytes32"
			}
		],
		"name": "transferApproved",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_from",
				"type": "address"
			},
			{
				"name": "_owner",
				"type": "address"
			},
			{
				"name": "_tokenVIN",
				"type": "string"
			},
			{
				"name": "_data",
				"type": "bytes"
			}
		],
		"name": "onERC721Received",
		"outputs": [
			{
				"name": "",
				"type": "bytes4"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"name": "_contract",
				"type": "address"
			},
			{
				"name": "_requiredSignatures",
				"type": "uint256"
			},
			{
				"name": "_authorities",
				"type": "address[]"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_from",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "_tokenVIN",
				"type": "string"
			},
			{
				"indexed": false,
				"name": "_data",
				"type": "bytes"
			}
		],
		"name": "UserRequestForSignature",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_tokenVIN",
				"type": "string"
			}
		],
		"name": "TransferCompleted",
		"type": "event"
	}
]
"""

token_abi = """
[
	{
		"constant": false,
		"inputs": [
			{
				"name": "_tokenVIN",
				"type": "string"
			},
			{
				"name": "_newTokenRegNumber",
				"type": "string"
			}
		],
		"name": "setTokenRegNumber",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "totalSupply",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_approved",
				"type": "address"
			},
			{
				"name": "_tokenVIN",
				"type": "string"
			}
		],
		"name": "approve",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_from",
				"type": "address"
			},
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_tokenVIN",
				"type": "string"
			},
			{
				"name": "_data",
				"type": "bytes"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_allowed",
				"type": "address"
			}
		],
		"name": "setPermissionsToRecover",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_from",
				"type": "address"
			},
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_tokenVIN",
				"type": "string"
			}
		],
		"name": "transferFrom",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_tokenVIN",
				"type": "string"
			},
			{
				"name": "_color",
				"type": "string"
			}
		],
		"name": "produce",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_tokenVIN",
				"type": "string"
			}
		],
		"name": "getSerializedData",
		"outputs": [
			{
				"name": "",
				"type": "bytes"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_from",
				"type": "address"
			},
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_tokenVIN",
				"type": "string"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_allowed",
				"type": "address"
			}
		],
		"name": "setPermissionsToDemolish",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_owner",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_tokenVIN",
				"type": "string"
			},
			{
				"name": "_newTokenColor",
				"type": "string"
			}
		],
		"name": "setTokenColor",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_tokenVIN",
				"type": "string"
			}
		],
		"name": "getTokenColor",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_tokenVIN",
				"type": "string"
			}
		],
		"name": "ownerOf",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_serializedData",
				"type": "bytes"
			}
		],
		"name": "deserealizeData",
		"outputs": [
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_tokenVIN",
				"type": "string"
			}
		],
		"name": "getApproved",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_owner",
				"type": "address"
			},
			{
				"name": "_tokenVIN",
				"type": "string"
			},
			{
				"name": "_serializedData",
				"type": "bytes"
			}
		],
		"name": "recoveryToken",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_tokenVIN",
				"type": "string"
			},
			{
				"name": "_color",
				"type": "string"
			},
			{
				"name": "_regNumber",
				"type": "string"
			}
		],
		"name": "produce",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_tokenVIN",
				"type": "string"
			}
		],
		"name": "getTokenRegNumber",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_tokenVIN",
				"type": "string"
			}
		],
		"name": "demolishToken",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "_from",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "_to",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "_tokenId",
				"type": "string"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "_owner",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "_approved",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "_tokenId",
				"type": "string"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "_tokenVIN",
				"type": "string"
			},
			{
				"indexed": false,
				"name": "_tokenColor",
				"type": "string"
			}
		],
		"name": "TokenColorChanged",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "_tokenVIN",
				"type": "string"
			},
			{
				"indexed": true,
				"name": "_tokenRegNumber",
				"type": "string"
			}
		],
		"name": "TokenRegNumberChanged",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_tokenVIN",
				"type": "string"
			}
		],
		"name": "TokenRecovered",
		"type": "event"
	}
]
"""