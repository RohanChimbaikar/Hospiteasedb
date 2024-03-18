from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('Regular', 'Regular'),
        ('ICU', 'Intensive Care Unit'),
        ('OR', 'Operating Room'),
        # Add more room types as needed
    ]

    number = models.CharField(max_length=20, unique=True)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES,default="Regular")
    capacity = models.PositiveIntegerField(default=1)
    floor = models.PositiveSmallIntegerField(blank=True,default=1)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    available = models.BooleanField(default=True)
    availability_start_date = models.DateField(blank=True, null=True)
    availability_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.number
