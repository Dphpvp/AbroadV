from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from user.forms import UserForm, UserUpdateForm
from user.models import User


# CreateView este o clasa dezvoltata de Django care va ajuta sa va definiti un obiect in baza de date
# daza de date si afisarea unui formular asociat modelului definit in models.py

# Principalele caracteristici

# Formular de creare: automat se genereaza un formular asociat modelului pentru a adauga un obiect nou

# Procesarea datelor: gestionati procesarea datelor introduse in formular prin validare.

# Redirectionare dupa crearea: in momentul in care obiectul este creat cu succes, utilizatorul este redir

# pe pagina dorita de noi

class UserCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'user/create_user.html'
    model = User
    form_class = UserForm  # in formular vor fi toate campurile
    success_url = reverse_lazy('home')
    permission_required = 'user.add_user'


# List view este o clasa dezvoltata de Django pentru afisarea unei liste de obiecte dintr-un model in template.

# principale caracteristici:

# Gestionarea listei: automatizeaza procesul de preluare a listei de obiecte dintr-un model
# list view foloseste un sablon implicit dar el va permite sa il folositi pe al vostru

class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'user/list_of_users.html'
    model = User
    context_object_name = 'all_students'
    permission_required = 'student.view_list_of_students'


# UpdateView este o clasa generica din Django  care este utilizata pentru a afisa un formular cu scopul de a actualiza
# informatiile despre obiectul existent din baza de date.

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'user/update_user.html'
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('details-user')


# DeleteView este o clasa generica din Django care este utilizata pentru a sterge un obiect existent din baza de date

# O clasa generica este o clasa care este definnita cu parametri de tipuri variabile ce permit ca aceeasi clasa sa fie
# utilizata pentru diferite tipuri de date, oferind flexibilitae si reutilizare cod

# Beneficiile utilizarii claselor generice:

# 1. reducerea repetitiilor de cod
# 2. utilizarea principiilor DRY (Don't Repeat yourself)
# 2.1 Redundanta -> evitarea duplicarii de cod in diferite partie ale unei aplicatii. Daca exista un bloc de cod care este
# utilizat in mai multe locuri acesta trebuie refacut intr-o functie, metoda, clasa.
# 2.2 Refolosirea codului
# 2.3 Mentinerea coerentei si a coeziunii. -> Atunci cand o schimbare este necesara intr-o anumita functionalitate,
# aceasta trebuie facuta doar intr--un singur loc, asigurant coerenta si evitand discrepanta.


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'user/delete_user.html'
    model = User
    success_url = reverse_lazy('list-of-students')


class StudentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'user/details_user.html'
    model = User
