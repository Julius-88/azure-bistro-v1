from django.urls import path
from . import views

urlpatterns = [
    path('reserve/', views.reserve, name='reserve'),
    path('reserve_contact/', views.reserve_contact, name='reserve_contact'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('manage_reservation/', views.manage_reservation, name='manage_reservation'),
    path('delete_reservation/<int:id>/', views.delete_reservation, name='delete_reservation'),
    path('modify_reservation/<int:reservation_id>/', views.modify_reservation, name='modify_reservation'),
]
