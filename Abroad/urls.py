"""
URL configuration for Abroad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from userextend.forms import AuthenticationNewForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path("login/", views.LoginView.as_view(form_class=AuthenticationNewForm), name="login"),
    path('', include('django.contrib.auth.urls')),
    path('', include('user.urls')),
    path('', include('userextend.urls')),
    path('notes/',include('notes.urls')),
    path('utilities/', include('utilities.urls')),
    path('',include('notes.urls')),
#>>>>>>> parent of 20ef0a2 (update about, login views, notes app, scrips, css, God knows what else)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


