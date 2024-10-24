//to connect to blockchain with front end
App={
    web3Provider: null, 
    contracts: {},
    //whenever you open index.html,this function is called
    init: async function(){
        return await App.initWeb3();
    },
    //initWeb3 is called by init function to initialise web3 provider
    initWeb3: async function(){
        //check for metamask
        if(window.web3){
            App.web3Provider=window.web3.currentProvider;//metamask will be attached
        }else{
            App.web3Provider = new Web3.providers.HttpProvider('http://localhost:7545');
          }
          web3=new Web3(App.web3Provider);
          return App.initContract();
    },
    //initContract is called by initWeb3 to initialise the contract
    initContract:async function(){
        //specify the artifact
        $.getJSON('voting.json',function(data){
            var votingArtifact=data;
            App.contracts.voting=TruffleContract(votingArtifact);//set contract 
            App.contracts.voting.setProvider(App.web3Provider);//set metamask
            
             return App.displayVotes();
        });
        return App.bindEvents();
    },
    //bindEvents is called by initContract
    bindEvents:function(){
        $(document).on('click','.btn-vote',App.handleVote);
    },
    //displayVotes is called by initContract
    //this function is displaying votes on the front end
    displayVotes:function(){
        var votingInstance;
        //connect with contract ->that instance we have to store
        App.contracts.voting.deployed().then(function(instance){
            votingInstance=instance;//instance is stored
            return votingInstance.viewVotes.call();//calling the solidity function
        }).then(function(votes){//votes of 3 leaders
            document.getElementById('v1').innerHTML=votes[0]['c'][0];
            document.getElementById('v2').innerHTML=votes[1]['c'][0];
            document.getElementById('v3').innerHTML=votes[2]['c'][0];

        }).catch(function(err){
            console.log(err.message);
        })
    },
    handleVote:function(){
        event.preventDefault();

        var votingInstance;
        var id=parsInt($(event.target).data('id'));
        console.log(id);
        //from which account ,we have to make transaction
        web3.eth.getAccounts(function(error,accounts){
            if(error){
                console.log(error);
            }
            var account=accounts[0];
            console.log(account);

            App.contracts.voting.deployed().then(function(instance){
                votingInstance=instance;
                return votingInstance.castVote(id,{from:account});
            }).then(function(result){
                console.log(result);
                document.getElementById('add').innerHTML=account;
                return App.displayVotes();
            }).catch(function(err){
                console.log(err.message);
            })
        }) 
    }
};
//whenever you open index.html-App.init() will be called
$(function(){
    $(window).load(function(){
        App.init();
    });
});