from django.contrib import admin
from .models import Invoice, BillingProfile, Item

# Register your models here.

admin.site.register(Invoice)
admin.site.register(BillingProfile)
admin.site.register(Item)

