from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'mobile_number', 'email', 'special_request', 'date', 'time', 'guests']
