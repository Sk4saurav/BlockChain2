// SPDX-License-Identifier: MIT
pragma solidity >=0.8.19 <0.9.0;

contract demo {
uint sum;
function add(uint a,uint b) public{
sum=a+b;
}
function result() public view returns(uint){
return(sum);
}
}
 