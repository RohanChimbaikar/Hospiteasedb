from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_status(self):
        if self.quantity <= 0:
            return 'OUT_OF_STOCK'
        elif self.quantity <= 10:
            return 'RUNNING_OUT'
        else:
            return 'IN_STOCK'
