from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from user.forms import UserForm, UserUpdateForm
from user.models import User


class UserCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'user/create_user.html'
    model = User
    form_class = UserForm  # in formular vor fi toate campurile
    success_url = reverse_lazy('home')
    permission_required = 'user.add_user'


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'user/list_of_users.html'
    model = User
    context_object_name = 'all_users'
    permission_required = 'user.view_list_of_users'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'user/update_user.html'
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('details-user')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'user/delete_user.html'
    model = User
    success_url = reverse_lazy('list-of-users')


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'user/details_user.html'
    model = User
