from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ReservationForm
from .models import Reservation

def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            # Send confirmation email
            # ...
            return redirect('confirm', reservation_id=reservation.pk)
    else:
        form = ReservationForm()
    return render(request, 'reserve.html', {'form': form})

def confirm(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    return render(request, 'confirm.html', {'reservation': reservation})

def admin_view(request):
    # Add authentication check
    reservations = Reservation.objects.all().order_by('-date', '-time')
    return render(request, 'admin_view.html', {'reservations': reservations})

def reserve(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'reserve.html', context)
