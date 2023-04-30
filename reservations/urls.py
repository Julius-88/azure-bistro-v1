from django.urls import path
from . import views

urlpatterns = [
    path('reserve/', views.reserve, name='reserve'),
    path('reserve_contact/', views.reserve_contact, name='reserve_contact'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('manage_reservation/', views.manage_reservation, name='manage_reservation'),
]
