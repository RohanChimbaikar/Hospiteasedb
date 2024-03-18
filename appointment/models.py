# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment with {self.doctor} on {self.date} at {self.time} for {self.name}"