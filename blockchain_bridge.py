from web3 import Web3, HTTPProvider
from contracts_abi import token_abi, home_bridge_abi, foreign_bridge_abi
import time


class Bridge:
    def __init__(self, private_key, s_token, home_bridge, k_token, foreign_bridge):
        self.kovan_w3 = Web3(HTTPProvider('https://kovan.infura.io/'))
        self.sokol_w3 = Web3(HTTPProvider('https://sokol.poa.network/'))
        self.bridge_account = self.kovan_w3.eth.account.privateKeyToAccount(private_key)

        s_token_address = Web3.toChecksumAddress(s_token)
        self.s_token = self.sokol_w3.eth.contract(address=s_token_address, abi=token_abi)
        home_bridge_address = Web3.toChecksumAddress(home_bridge)
        self.home_bridge = self.sokol_w3.eth.contract(address=home_bridge_address, abi=home_bridge_abi)

        k_token_address = Web3.toChecksumAddress(k_token)
        self.k_token = self.kovan_w3.eth.contract(address=k_token_address, abi=token_abi)
        foreign_bridge_address = Web3.toChecksumAddress(foreign_bridge)
        self.foreign_bridge = self.kovan_w3.eth.contract(address=foreign_bridge_address, abi=foreign_bridge_abi)

        self.last_home_block = 0
        self.last_foreign_block = 0

    def bridge_to_kovan(self):
        while True:
            events = self.get_events(self.sokol_w3, self.home_bridge, self.last_home_block)
            for event in events:
                self.send_transaction(self.kovan_w3, self.foreign_bridge, event)
            time.sleep(3)

    def bridge_to_sokol(self):
        while True:
            events = self.get_events(self.kovan_w3, self.foreign_bridge, self.last_foreign_block)
            for event in events:
                self.send_transaction(self.sokol_w3, self.home_bridge, event)
            time.sleep(3)

    def send_transaction(self, w3, bridge_contract, event):
        nonce = w3.eth.getTransactionCount(self.bridge_account.address)
        tx = {
            'gas': 7000000,
            'gasPrice': Web3.toWei(1, 'gwei'),
            'nonce': nonce
        }
        transaction = bridge_contract.functions.transferApproved(
            event['args']['_from'],
            event['args']['_tokenVIN'],
            event['args']['_data'],
            event['transactionHash']
        ).buildTransaction(tx)

        signed_tx = self.bridge_account.signTransaction(transaction)
        tx_hash = w3.eth.sendRawTransaction(signed_tx['rawTransaction'])
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    def get_events(self, w3, contract, last_block):
        to_block = w3.eth.getBlock('latest')['number']
        filter_params = {
            'fromBlock': last_block,
            'toBlock': to_block,
            'address': contract.address
        }
        logs = w3.eth.getLogs(filter_params)

        events = []

        for log in logs:
            tx_hash = log['transactionHash']
            receipt = w3.eth.getTransactionReceipt(tx_hash)
            log_events = contract.events.UserRequestForSignature().processReceipt(receipt)
            events.extend(log_events)

        if w3 == self.sokol_w3:
            self.last_home_block = to_block
        else:
            self.last_foreign_block = to_block

        return events
