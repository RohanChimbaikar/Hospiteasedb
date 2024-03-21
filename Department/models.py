from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Department(models.Model):
    DEPARTMENT_CHOICES = [
    ('CARDIOLOGY', 'Cardiology'),
    ('PEDIATRICS', 'Pediatrics'),
    ('SURGERY', 'Surgery'),
    ('NEUROLOGY', 'Neurology'),
    ('ORTHOPEDICS', 'Orthopedics'),
    ('ONCOLOGY', 'Oncology'),
    ('DERMATOLOGY', 'Dermatology'), 
    ('GASTROENTEROLOGY', 'Gastroenterology'),
    ('UROLOGY', 'Urology'),
    ('GYNECOLOGY', 'Gynecology'),  # Corrected to uppercase
    ('OPHTHALMOLOGY', 'Ophthalmology'),
    ('OTOLARYNGOLOGY', 'Otolaryngology'),
    ('RADIOLOGY', 'Radiology'),
    ('PATHOLOGY', 'Pathology'),
    ('EMERGENCY_MEDICINE', 'Emergency Medicine'),
    ('ANESTHESIOLOGY', 'Anesthesiology'),
    ('PSYCHIATRY', 'Psychiatry'),
    ('INTERNAL_MEDICINE', 'Internal Medicine'),
    ('FAMILY_MEDICINE', 'Family Medicine'),
    ('PUBLIC_HEALTH', 'Public Health'),
    ]

    name = models.CharField(max_length=100,choices=DEPARTMENT_CHOICES)
    description = models.TextField()
    head_of_department = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='department_headed')
    location = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    doctors = models.ManyToManyField(User, related_name='departments')


    def __str__(self):
        return self.name

class Qualification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualifications = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.qualifications}"