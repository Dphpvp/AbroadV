    function sendMessage() {
        var userInput = document.getElementById('user-input').value;


        appendToChatHistory('User: ' + userInput);


        $.ajax({
            type: 'POST',
            url: '/chat/',
            data: {
                'input': userInput,
                'csrfmiddlewaretoken': '{{ csrf_token }}',
            },
            success: function (response) {
                // Append OpenAI's response to the chat history
                appendToChatHistory('AI: ' + response.response);
            },
            error: function (error) {
                console.log('Error:', error);
            }
        });


        document.getElementById('user-input').value = '';
    }

    function appendToChatHistory(message) {
        var chatHistory = document.getElementById('chat-history');
        chatHistory.innerHTML += '<p>' + message + '</p>';
    }