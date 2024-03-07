let messageContainer = $(".msg-container");
let inputMessage = $('.input-message');
const sentForm = $('#sent-form');
const searchContact = $("#search");
const USER_ID = $('#logged-in-user').val();


let endpoint = "ws://" + location.host + location.pathname
var sc = new WebSocket(endpoint);
console.log(location.pathname);


messageContainer.animate({
    scrollTop: $('.msg-container')[0].scrollHeight
})



sc.onopen = async (e) => {
    console.log("connection connected!", e);
    // This function sends messages to the backend
    sentForm.on('submit', function (e) {
        e.preventDefault();
        let message = inputMessage.val();
        let send_to = get_active_other_user_id();
        let thread_id = get_active_thread_id();

        let data = {
            'type': 'message',
            'message': message,
            'sent_by': USER_ID,
            'send_to': send_to,
            'thread_id': thread_id
        }
        data = JSON.stringify(data);
        sc.send(data);
        $(this)[0].reset();
    })

    // Here the function search the contact and made connection
    searchContact.on("keyup", function (e) {
        let srch = $('.search-box').val();
        console.log(srch)
        let data = {
            'type': 'search',
            'search': srch,
        }
        data = JSON.stringify(data);
        sc.send(data);
    })
}

sc.onmessage = async (e) => {
    let data = JSON.parse(e.data);
    if (data.identity === 'search-user') {
        console.log("Search is working!")
    }
    else {
        let message = data['message'];
        let sent_by_id = data['sent_by'];
        let thread_id = data['thread_id'];
        newMessage(message, sent_by_id, thread_id);
    }
}

sc.onerror = async (e) => {
    console.log("error on connection!");
}

sc.onclose = async (e) => {
    console.log("Connection Closed!");
}


//Here message is updated on front end side
function newMessage(message, sent_by_id, thread_id) {
    if ($.trim(message) === '') {
        return false;
    }

    let messageElement;
    let chat_id = 'chat_' + thread_id;
    if (sent_by_id == USER_ID) {
        messageElement = `<div class="message right">${message}</div>`;
    }
    else {
        messageElement = `<div class="message left">${message}</div>`;
    }

    //This code to show last message sent
    let messageContainer = $('.message-section[chat-id="' + chat_id + '"] .msg-container')
    messageContainer.append($(messageElement));

    //this code to stick scrollbar to the bottom 
    messageContainer.animate({
        scrollTop: $('.msg-container')[0].scrollHeight
    })
}

$('.contact').on('click', function () {
    $('.contact-list .active').removeClass('active')
    $(this).addClass('active')

    // message wrappers
    let chat_id = $(this).attr('chat-id')
    $('.message-section.is_active').removeClass('is_active')
    $('.message-section[chat-id="' + chat_id + '"]').addClass('is_active')

})

function get_active_other_user_id() {
    let other_user_id = $('.message-section.hide.is_active').attr('other-user-id')
    other_user_id = $.trim(other_user_id)
    return other_user_id
}

function get_active_thread_id() {
    let chat_id = $('.message-section.hide.is_active').attr('chat-id');
    let thread_id = chat_id.replace('chat_', '');
    return thread_id
}