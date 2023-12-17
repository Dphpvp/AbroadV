from django.http import request
from django.shortcuts import render
from django.template import context
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from Abroad.openai_utils import generate_openai_response


# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'


def home_view():
    return render(request, 'home/homepage.html', context)


@csrf_exempt  # To allow POST requests without CSRF token for simplicity (customize as needed)
def chat_view(request):
    if request.method == 'POST':
        # Get the user's input from the request
        user_input = request.POST.get('input', '')

        # Call the OpenAI API to generate a response
        response = generate_openai_response(user_input)

        # Return the response as JSON
        return JsonResponse({'response': response})

    return JsonResponse({'error': 'Invalid request method'})


def chat_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        response = generate_openai_response(user_input)
        return render(request, 'home/homepage.html', {'response': response})

    return render(request, 'home/homepage.html')
