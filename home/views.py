from django.http import request
from django.shortcuts import render
from django.template import context
from django.views.generic import TemplateView


# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'


def home_view():
    return render(request, 'home/homepage.html', context)


