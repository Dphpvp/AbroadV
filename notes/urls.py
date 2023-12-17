from django.urls import path

from django.urls import path

from notes import views
from notes.views import add_note, notes_list

urlpatterns = [
    path('create-notes/', add_note, name='create-notes'),
    path('list-of-notes/', views.notes_list, name='list-of-notes'),
]
