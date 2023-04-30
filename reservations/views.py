import random
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Reservation

def reserve(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        reservation_number = (random.randint(1, 100000))
        # Create a new reservation using the Reservation model
        reservation = Reservation(date=date, time=time, guests=guests, reservation_number=reservation_number)
        reservation.save()

        return redirect('reserve_contact')

    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'reservations/reserve.html', context)

def reserve_contact(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'reservations/reserve_contact.html', context)

def sign_in(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'reservations/sign_in.html', context)


# Modifying Reservation
def manage_reservation(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    # Render the reservation management page and pass the reservation data
    return render(request, 'reservations/manage_reservation.html', context)

