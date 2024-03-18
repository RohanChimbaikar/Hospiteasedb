from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
