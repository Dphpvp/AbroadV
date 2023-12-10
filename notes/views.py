from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from notes.forms import NotesForm
from .models import Notes


class NotesCreateView(LoginRequiredMixin, CreateView):
    template_name = 'notes/create_note.html'
    model = Notes
    form_class = NotesForm
    success_url = reverse_lazy('list_of_notes')


class NotesListView(LoginRequiredMixin, ListView):
    template_name = 'notes/list_of_notes.html'
    model = Notes
    context_object_name = 'all_notes'
