from django.contrib.auth.models import User
from django.db import models
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
    # profile_picture = models.ImageField(upload_to='media/profile_pictures', null=True, blank=True)
    avatar = models.ImageField(
        default='avatar.jpg', # default avatar
        upload_to='profile_avatars', # dir to store the image
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.user.username


    def save(self, *args, **kwargs):
     super().save(*args, **kwargs)
     img = Image.open(self.avatar.path)
     if img.height > 150 or img.width > 150:
            output_size = (150, 150)
        # create a thumbnail
            img.thumbnail(output_size)
        
        # overwrite the large image
            img.save(self.avatar.path)
