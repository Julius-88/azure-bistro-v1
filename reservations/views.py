import random
from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.urls import reverse
from .models import Reservation
from django.http import Http404

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

def reserve_contact(request):
    return render(request, 'reserve_contact.html')


def confirm(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    return render(request, 'confirm.html', {'reservation': reservation})

def admin_view(request):
    # Add authentication check
    reservations = Reservation.objects.all().order_by('-date', '-time')
    return render(request, 'admin_view.html', {'reservations': reservations})

# Modifying Reservation
def manage_reservation(request, reservation_number):
    try:
        reservation = Reservation.objects.get(reservation_number=reservation_number)
    except Reservation.DoesNotExist:
        raise Http404("Reservation does not exist")

    # Render the reservation management page and pass the reservation data
    return render(request, 'manage_reservation.html', {'reservation': reservation})

def update_reservation(request, reservation_number):
    reservation = get_object_or_404(Reservation, reservation_number=reservation_number)
    
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')

        reservation.date = date
        reservation.time = time
        reservation.guests = guests
        reservation.save()

        return redirect(reverse('manage_reservation', args=[reservation_number]))
    
    return redirect('reserve')

def cancel_reservation(request, reservation_number):
    reservation = get_object_or_404(Reservation, reservation_number=reservation_number)

    if request.method == 'POST':
        reservation.delete()
        return redirect('reserve')

    return redirect('reserve')