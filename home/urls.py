from django.urls import path, include

from home import views
from home.views import chat_view

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('chat/', chat_view, name='chat'),
#    path('search/', search_view, name='search'),
    path('', include('about.urls')),
    path('', include('notes.urls')),
    path('', include('utilities.urls')),
]
