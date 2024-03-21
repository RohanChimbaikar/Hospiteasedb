# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)
    accepted = models.BooleanField(default=False)
    def __str__(self):
        date_str = self.date.strftime('%Y-%m-%d') if self.date else "Unknown date"
        start_time_str = self.start_time.strftime('%I:%M %p') if self.start_time else "Unknown start time"
        end_time_str = self.end_time.strftime('%I:%M %p') if self.end_time else "Unknown end time"
        
        return f"Appointment with Dr. {self.doctor.get_full_name()} on {date_str} from {start_time_str} to {end_time_str} for {self.name}"


from django.db import models
from django.contrib.auth.models import User

class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    time_slots = models.ManyToManyField(TimeSlot, related_name='doctors', blank=True)

    def __str__(self):
        return self.user.get_full_name()
