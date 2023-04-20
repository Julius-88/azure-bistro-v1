from django.shortcuts import render
from django.conf import settings

def reserve(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'reserve.html', context)
