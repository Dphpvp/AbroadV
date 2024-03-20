from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from notes.models import Note

from notes.forms import NotesForm
from .models import Notes

#<<<<<<< HEAD

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-of-notes')  # Update to the correct URL name
    else:
        form = NoteForm()
#=======
#>>>>>>> parent of 20ef0a2 (update about, login views, notes app, scrips, css, God knows what else)

class NotesCreateView(LoginRequiredMixin, CreateView):
    template_name = 'notes/create_note.html'
    model = Notes
    form_class = NotesForm
    success_url = reverse_lazy('list_of_notes')


#<<<<<<< HEAD
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/list_of_notes.html', {'notes': notes})
#=======
class NotesListView(LoginRequiredMixin, ListView):
    template_name = 'notes/list_of_notes.html'
    model = Notes
    context_object_name = 'all_notes'
#>>>>>>> parent of 20ef0a2 (update about, login views, notes app, scrips, css, God knows what else)
