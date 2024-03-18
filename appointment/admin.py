from django.contrib import admin
from .models import Appointment

admin.site.register(Appointment)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'date', 'time', 'name', 'email', 'phone']
    search_fields = ['doctor', 'name', 'email', 'phone']
    list_filter = ['doctor', 'date', 'time']
