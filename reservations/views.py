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
    return render(request, 'reserve.html', context)

def confirm(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    return render(request, 'confirm.html', {'reservation': reservation})

def admin_view(request):
    # Add authentication check
    reservations = Reservation.objects.all().order_by('-date', '-time')
    return render(request, 'admin_view.html', {'reservations': reservations})
