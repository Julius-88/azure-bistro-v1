from django.urls import path
from . import views

urlpatterns = [
    path('reserve/', views.reserve, name='reserve'),
    path('reserve_contact/', views.reserve_contact, name='reserve_contact'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('manage_reservation/<int:reservation_number>/', views.manage_reservation, name='manage_reservation'),
    path('update_reservation/<int:reservation_number>/', views.update_reservation, name='update_reservation'),
    path('cancel_reservation/<int:reservation_number>/', views.cancel_reservation, name='cancel_reservation'),
]
