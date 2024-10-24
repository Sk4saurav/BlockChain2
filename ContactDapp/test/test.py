from web3 import Web3,HTTPProvider
import json

def connect_with_blockchain(account):
    #stage 1 where rpc server is available
    blockchainServer='http://127.0.0.1:7545'
    web3=Web3(HTTPProvider(blockchainServer))
    #stage2 Through which account we have to connect
    
    if account==0:
        web3.eth.defaultAccount=web3.eth.accounts[0]
    else:
        web3.eth.defaultAccount=account
    #stage 3 select your contract
    
    with open('../build/contracts/contact.json') as f:
        artifact_json=json.load(f)
        contract_abi=artifact_json['abi'] #application binary interface
        contract_address=artifact_json['networks']['5777']['address']
     #stage4 connect with contract   
    contract=web3.eth.contract(abi=contract_abi,address=contract_address)

    return (contract,web3)

try:
    contract,web3=connect_with_blockchain(0)
    tx_hash=contract.functions.insertContact("KSP","9997777745","sri@gmail.com","BIT Mesra").transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    print('contact information stored successfully')
except:
    print('This contact information is already available')

contract,web3=connect_with_blockchain(0)   
names,mobiles,emails,organizations=contract.functions.viewContacts().call() 
print(names)
print(mobiles)
print(emails)
print(organizations)
