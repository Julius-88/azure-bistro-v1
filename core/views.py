from django.shortcuts import render
from django.conf import settings

def index(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'index.html', context)

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    return render(request, 'contact.html')

