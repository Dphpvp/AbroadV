from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-of-notes')  # Update to the correct URL name
    else:
        form = NoteForm()

    return render(request, 'notes/create_note.html', {'form': form})


def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/list_of_notes.html', {'notes': notes})
