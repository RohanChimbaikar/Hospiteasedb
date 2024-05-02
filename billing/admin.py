from django.contrib import admin
from .models import HospitalInvoice,Service


# Register your models here.
admin.site.register(HospitalInvoice)
admin.site.register(Service)
