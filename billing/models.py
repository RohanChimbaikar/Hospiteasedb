from django.db import models
from django.contrib.auth.models import User

class BillingProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Other fields related to billing profile (e.g., insurance information)

    def __str__(self):
        return f'Billing Profile for {self.user.username}'

class Invoice(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status_choices = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    due_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Invoice for {self.patient.username} - {self.date_created}'

class Item(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def line_total(self):
        return self.quantity * self.unit_price

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=20, default='pending')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Payment of {self.amount_paid} for {self.invoice}'
