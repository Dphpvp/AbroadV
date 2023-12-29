from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import requests


class UtilitiesTemplateView(TemplateView):
    template_name = 'utilities/utilities.html'





def currency_exchange(request):
    # Get parameters from the request
    from_currency = request.GET.get('from_currency', 'USD')
    to_currency = request.GET.get('to_currency', 'USD')
    amount = float(request.GET.get('amount', 1.0))

    api_key = 'cur_live_whWesVHTRZ309SvavTelq2andPDiilxRbB2SvmSv'

    # Make the API request
    response = requests.get(f'https://open.er-api.com/v6/latest/{from_currency}?apikey={api_key}')
    data = response.json()

    # Extract exchange rate
    exchange_rate = data['rates'].get(to_currency, 1.0)

    # Calculate converted amount
    converted_amount = amount * exchange_rate

    # Prepare response
    response_data = {
        'exchange_rate': exchange_rate,
        'converted_amount': converted_amount
    }

    return JsonResponse(response_data)
