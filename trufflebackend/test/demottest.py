
from web3 import Web3,HTTPProvider
import json

def connect_with_blockchain(acc):
    rpcServer="HTTP://127.0.0.1:7545"
    web3=Web3(HTTPProvider(rpcServer))
    print('connected to blockchain')

    if acc==0:
        web3.eth.defaultAccount=web3.eth.accounts[0]
    else:
        web3.eth.defaultAccount=acc

        
    with open('../build/contracts/demo.json') as f:
        contract_json=json.load(f)
        contract_abi=contract_json['abi']
        contract_address=contract_json['networks']['5777']['address']

    contract=web3.eth.contract(address=contract_address,abi=contract_abi)
        
    return (contract,web3)
try:
    contract,web3=connect_with_blockchain(0)
    tx_hash=contract.functions.add(2,3).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    output=contract.functions.result().call()
    print(output)
except:
    print('result not displayed')
    






