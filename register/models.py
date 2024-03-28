from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from PIL import Image

class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    medical_school = models.CharField(max_length=100, null=True, blank=True)
    license_number = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(
        default='avatar.jpg', # default avatar
        upload_to='profile_avatars', # dir to store the image
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Resize avatar image if necessary
        super().save(*args, **kwargs)
        img = Image.open(self.avatar.path)
        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
