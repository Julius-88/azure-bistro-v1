from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    special_request = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    table = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return f'{self.name} ({self.date} {self.time})'
