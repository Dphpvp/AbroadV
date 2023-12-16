from django.urls import path

from notes import views

from django.urls import path

urlpatterns = [
    path('create-notes/', views.NotesCreateView.as_view(), name='create-notes'),
    path('list-of-notes/', views.NotesListView.as_view(), name='list-of-notes'),
]
