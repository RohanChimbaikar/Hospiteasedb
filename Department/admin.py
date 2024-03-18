from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'head_of_department')

admin.site.register(Department, DepartmentAdmin)

class DepartmentInline(admin.TabularInline):
    model = Department.doctors.through
    extra = 1
    verbose_name = 'Department'

class UserAdmin(BaseUserAdmin):
    inlines = [DepartmentInline]
    search_fields = ('username', 'email')
    list_display = ('username', 'email', 'get_departments')
    
    


    def get_departments(self, obj):
        return ", ".join([department.name for department in obj.departments.all()])
    get_departments.short_description = 'Departments'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
