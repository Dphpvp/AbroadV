function addNote() {
    var noteContent = $('#note-input').val();

    // Make an AJAX request to the Django backend
    $.ajax({
        type: 'POST',
        url: '/notes/create-notes/',
        data: {
            'content': noteContent,
            'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val()  // Corrected selector
        },
        success: function (response) {
            // Reload the notes container after successfully adding a note
            getNotes();
            // Clear the note input field
            $('#note-input').val('');
        },
        error: function (error) {
            console.log('Error:', error);
        }
    });
}

function getNotes() {
    // Make an AJAX request to the Django backend
    $.ajax({
        type: 'GET',
        url: '/notes/list-of-notes/',  // Updated URL to match the notes app
        success: function (response) {
            // Update the notes container with the retrieved notes
            $('#notes-list').html(response);
        },
        error: function (error) {
            console.log('Error:', error);
        }
    });
}