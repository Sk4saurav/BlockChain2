from flask import Flask,render_template,request#bridge between html and python
from web3 import Web3,HTTPProvider #web3 is a bridge between python and blockchain
import json
def connect_with_blockchain(account):
    blockchainServer='HTTP://127.0.0.1:7545'
    web3=Web3(HTTPProvider(blockchainServer))
    if account==0:
        web3.eth.defaultAccount=web3.eth.accounts[0]
    else:
        web3.eth.defaultAccount=account
    
    with open('../build/contracts/contact.json') as f:
        contact_json=json.load(f)
        contract_abi=contact_json['abi']
        contract_address=contact_json['networks']['5777']['address']
        
    contract=web3.eth.contract(address=contract_address,abi=contract_abi)
        
      
    return(contract,web3)
        
    
#create an object
app=Flask(__name__)
@app.route('/')#handler handling home '/'
def homepage():#handler function
    return render_template('index.html')
@app.route('/insertcontact',methods=["post"])#get the data from html
def insertcontact():
    name=request.form['name']
    mobile=request.form['mobile']
    email=request.form['email']
    org=request.form['org']
    print(name,mobile,email,org)
    #access blockchain
    try:
         contract,web3=connect_with_blockchain(0)
         tx_hash=contract.functions.insertContact(name,mobile,email,org).transact()
         web3.eth.wait_for_transaction_receipt(tx_hash)
         return render_template('index.html',res='this contact is stored successfully')
    except:
        return render_template('index.html',error='this contact already exists')
    
                
    
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)
    
    