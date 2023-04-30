import random
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Reservation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def reserve(request):
    if not request.user.is_authenticated:
        return redirect('sign_in')
    
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        reservation_number = (random.randint(1, 100000))
        # Create a new reservation using the Reservation model
        reservation = Reservation(date=date, time=time, guests=guests, reservation_number=reservation_number)
        reservation.save()

        return redirect('reserve')

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
    if request.method == 'POST':
        # Get the username and password from the form data
        username = request.POST['user_name']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is not None:
            # Log the user in
            login(request, user)
            # Redirect the user to the reservation page
            return redirect('reserve')
        else:
            # Return an error message
            context = {
                'error_message': 'Invalid login credentials.',
                'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
                }
            return render(request, 'reservations/sign_in.html', context)
    context = {
                'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
                }
    # Render the sign-in page if the request method is not POST
    return render(request, 'reservations/sign_in.html', context)

def register(request):
    if request.method == 'POST':
        # Get the username and password from the form data
        user_name = request.POST['user_name']
        password = request.POST['password']
        # Check if the username is already taken
        if User.objects.filter(username=user_name).exists():
            # Return an error message
            context = {
                'error_message': 'Username is already taken.',
                'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
                }
            return render(request, 'reservations/register.html', context)
        # Create a new user with the given username and password
        user = User.objects.create_user(username=user_name, password=password)
         # Redirect the user to the reservation page
        return redirect('sign_in')
     # Render the register page if the request method is not POST
    return render(request, 'reservations/register.html')


# Modifying Reservation
def manage_reservation(request):
    reservations = Reservation.objects.all();
    context = {
        'reservations': reservations,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    # Render the reservation management page and pass the reservation data
    return render(request, 'reservations/manage_reservation.html', context)
