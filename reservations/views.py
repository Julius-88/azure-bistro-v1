import random
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Reservation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReservationForm


@login_required
def reserve(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        reservation_number = (random.randint(1, 100000))
        # Create a new reservation using the Reservation model
        reservation = Reservation(user=request.user, date=date, time=time, guests=guests, reservation_number=reservation_number)
        reservation.save()

        return redirect('reserve')
    # Check if the user is authenticated
    if request.user.is_authenticated:
        context = {
            'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
        }
        return render(request, 'reservations/reserve.html', context)
    else:
        return redirect('sign_in')

def reserve_contact(request):
    if request.method == 'POST':
        user = request.user
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        special_request = request.POST.get('message')
        reservation_number = (random.randint(1, 100000))

        reservation = Reservation(
            user=user,
            date=date,
            time=time,
            guests=guests,
            reservation_number=reservation_number,
            name=name,
            email=email,
            special_request=special_request
        )
        reservation.save()

        # Redirect or display a success message
        return redirect('index')
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'reservations/reserve_contact.html', context)

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('reserve')
    
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
    context = {
                'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
                }
     # Render the register page if the request method is not POST
    return render(request, 'reservations/register.html', context)


# Modifying Reservation
@login_required
def manage_reservation(request):
    reservations = Reservation.objects.filter(user=request.user)
    modified_reservations = set()
    
    if request.method == 'POST':
        reservation_id = request.POST.get('reservation_id')
        reservation = Reservation.objects.get(id=reservation_id)
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation updated successfully')
            modified_reservations.add(reservation)
        else:
            messages.error(request, 'Invalid form submission')

    context = {
        'reservations': reservations,
        'modified_reservations': modified_reservations,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
        'css_files': ['/static/css/global_styles.css', '/static/css/form_styles.css'],
    }
    
    return render(request, 'reservations/manage_reservation.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')


def delete_reservation(request, id):
    reservation = Reservation.objects.get(id=id)
    reservation.delete()
    messages.success(request, 'Reservation deleted successfully')
    return redirect('manage_reservation')

@login_required
def modify_reservation(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation updated successfully')
            return redirect('manage_reservation')
    else:
        form = ReservationForm(instance=reservation)

    context = {
        'form': form,
        'reservation': reservation,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
        'css_files': ['/static/css/global_styles.css', '/static/css/form_styles.css'],
    }

    return render(request, 'reservations/modify_reservation.html', context)