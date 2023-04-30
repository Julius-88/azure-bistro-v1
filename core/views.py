from django.shortcuts import render
from django.conf import settings

def index(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'core/index.html', context)

def menu(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'core/menu.html', context)

def contact(request):
    google_maps_api_key = settings.GOOGLE_MAPS_API_KEY
    context = {
        'google_maps_api_key': google_maps_api_key,
    }
    return render(request, 'core/contact.html', context)
