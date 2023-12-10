from django.urls import path

from student import views

urlpatterns = [
    path('create_user/', views.UserCreateView.as_view(), name='create-user'),
    path('list_of_users/', views.StudentListView.as_view(), name='list-of-user'),
    path('update_users/<int:pk>/', views.UserUpdateView.as_view(), name='update-user'),
    path('delete_users/<int:pk>/', views.UserDeleteView.as_view(), name='delete-user'),
    path('details_users/<int:pk>/', views.UserDetailView.as_view(), name='details-user'),
]