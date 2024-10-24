// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract voting {
  uint[3] private votes;//pubic leaders
  mapping(address=>bool) public voters;//who have polled

  constructor() public {//contract is deployed and resetting the votes
    votes[0]=0;
    votes[1]=0;
    votes[2]=0;
  }
  //function to cast vote
  function castVote(uint id)public{
    require(!voters[msg.sender]);// Ex. wallet no 0x123-!False=True
    voters[msg.sender]=true;// 0X123 regsitered i.e voted
    if(id==0){//Narendra Modi
      votes[0]+=1;
    } else if(id==1){//Vadimir Putin
      votes[1]+=1;
    } else if(id==2){//Joe Biden
      votes[2]+=1;
    }
  }
  //displaying how many votes have been polled for each leader
  function viewVotes() public view returns(uint[3] memory){
    return(votes);
  }


}
