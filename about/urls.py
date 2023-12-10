from django.urls import path

from about.views import AboutTemplateView

urlpatterns = [
    path('', AboutTemplateView.as_view(), name='about'),

]