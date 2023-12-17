    function sendMessage() {
        var userInput = document.getElementById('user-input').value;

        // Append user's message to the chat history
        appendToChatHistory('User: ' + userInput);

        // Make an AJAX request to your Django backend
        $.ajax({
            type: 'POST',
            url: '/chat/',
            data: {
                'input': userInput,
                'csrfmiddlewaretoken': '{{ csrf_token }}',  // Include CSRF token for security
            },
            success: function (response) {
                // Append OpenAI's response to the chat history
                appendToChatHistory('AI: ' + response.response);
            },
            error: function (error) {
                console.log('Error:', error);
            }
        });

        // Clear the input field
        document.getElementById('user-input').value = '';
    }

    function appendToChatHistory(message) {
        var chatHistory = document.getElementById('chat-history');
        chatHistory.innerHTML += '<p>' + message + '</p>';
    }