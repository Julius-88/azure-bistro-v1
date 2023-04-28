from django.shortcuts import render
from django.conf import settings

def index(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'index.html', context)

def menu(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'menu.html', context)

def contact(request):
    google_maps_api_key = settings.GOOGLE_MAPS_API_KEY
    emailjs_public_key = settings.EMAILJS_PUBLIC_KEY
    context = {
        'EMAILJS_PUBLIC_KEY': emailjs_public_key,
        'google_maps_api_key': google_maps_api_key,
    }
    return render(request, 'contact.html', context)
