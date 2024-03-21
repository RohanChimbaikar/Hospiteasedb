# custom_tags.py

from django import template

register = template.Library()

@register.filter
def get_departments_display(user):
    return ', '.join(department.name for department in user.department_set.all() if department)
