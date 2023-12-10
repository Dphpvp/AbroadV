from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class AboutTemplateView(TemplateView):
    template_name = 'about/about.html'


def about_us(request):
    return render(request, 'about/about.html', context)


