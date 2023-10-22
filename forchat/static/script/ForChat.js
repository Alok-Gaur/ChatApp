let messageContainer = $(".msg-container");
let inputMessage = $('.input-message');
const sentForm = $('#sent-form');
var sc = new WebSocket("ws://127.0.0.1:8000/message");

// console.log(message);
sc.onopen = (e) => {
    console.log("connection connected!", e);
    sentForm.on('submit', function (e) {
        e.preventDefault();
        let message = inputMessage.val();
        newMessage(message);
        let data = {
            'message': message
        }
        data = JSON.stringify(data);
        sc.send(data);
        $(this)[0].reset();
    })
}

sc.onmessage = (e) => {
    console.log(e);
    // sentForm.addEventListener('submit', (event)=>{
    //     console.log(event.data);
    // })

}

sc.onerror = (e) => {
    console.log("error on connection!");
}

sc.onclose = (e) => {
    console.log("Connection Closed!");
}


//Here message is updated on front end side
function newMessage(message) {
    if ($.trim(message) === '') {
        return false;
    }

    let messageElement = `
        <div class="message right">${message}</div>
    `
    //This code to show last message sent
    messageContainer.append($(messageElement));

    //this code to stick scrollbar to the bottom 
    messageContainer.animate({
        scrollTop: $('.msg-container')[0].scrollHeight
    })

}