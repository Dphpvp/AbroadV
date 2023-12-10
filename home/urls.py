
from django.urls import path, include

from home import views


urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('', include('about.urls')),
    path('', include('notes.urls')),
]