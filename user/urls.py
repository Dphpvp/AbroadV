from django.urls import path

from user import views

urlpatterns = [
    path('list_of_users/', views.UserListView.as_view(), name='list-of-user'),
    path('update_users/<int:pk>/', views.UserUpdateView.as_view(), name='update-user'),
    path('delete_users/<int:pk>/', views.UserDeleteView.as_view(), name='delete-user'),
    path('account_details/', views.UserDetailView.as_view(), name='account-details'),
]