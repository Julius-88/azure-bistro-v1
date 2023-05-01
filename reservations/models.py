from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    special_request = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

    def __str__(self):
        return f'{self.name} ({self.date} {self.time})'
