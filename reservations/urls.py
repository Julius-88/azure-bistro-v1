from django.urls import path
from . import views

urlpatterns = [
    path('reserve/', views.reserve, name='reserve'),
    path('confirm/<int:reservation_id>/', views.confirm, name='confirm'),
    path('admin_view/', views.admin_view, name='admin_view'),
]
