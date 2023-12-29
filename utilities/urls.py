from django.urls import path
from utilities.views import UtilitiesTemplateView

urlpatterns = [
    path('', UtilitiesTemplateView.as_view(), name='utilities'),
]
