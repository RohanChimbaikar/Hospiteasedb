from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity', 'date_added')
    list_filter = ('quantity', 'date_added')
    search_fields = ('name', 'description')
    sortable_by = ('name', 'quantity', 'date_added')

admin.site.register(Product, ProductAdmin)
