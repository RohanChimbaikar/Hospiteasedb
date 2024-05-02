from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class HospitalInvoice(models.Model):
    date = models.DateField()
    invoice_number = models.CharField(max_length=20)
    patient_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='invoices')
    total_amount_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid')
    services = models.ManyToManyField(Service, blank=True)

    def __str__(self):
        return f"Invoice Number: {self.invoice_number}, Patient: {self.patient_name}"
