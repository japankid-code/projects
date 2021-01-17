
var facebookProfile = {
    name: "jake",
    friends: 69,
    messages: ["lorem ipsum dolor sit amet.", "lorem ipsum dolor sit amet.", "lorem ipsum dolor sit amet."],
    postMessage: function(message) {
        facebookProfile.messages.push(message);
    },
    deleteMessage: function(index){
        facebookProfile.messages.splice(index, 1);
    },
    addFriend: function() {
        facebookProfile.friends+=1;
    },
    removeFriend: function(){
        if (facebookProfile.friends>0)
            facebookProfile.friends-=1;
    }
    
}