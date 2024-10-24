// SPDX-License-Identifier: MIT
pragma solidity >=0.8.19 <0.9.0;

contract contact {
  address owner;
  string[] names;
  string[] mobiles;
  string[] emails;
  string[] organizations;
  mapping(string=>bool) _contacts;
  constructor() public
  {
    owner=msg.sender;
  }
modifier onlyOwner{
  require(owner==msg.sender);
  _;
  
}
//inserting the contact into the daap
function insertContact(string memory name,string memory mobile,string memory email,string memory org)public onlyOwner{
  require(!_contacts[mobile]);
  names.push(name);
  mobiles.push(mobile);
  emails.push(email);
  organizations.push(org);
  _contacts[mobile]=true;
}
//read contact from blockchain
function viewContacts() public onlyOwner view returns(string[] memory,string[] memory,string[] memory,string[] memory) {
  return(names,mobiles,emails,organizations);
}
}