from django.contrib import admin
from .models import Employee


# Register your models here.

admin.site.register(Employee)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('role', 'first_name', 'last_name','manager')
    fields = ['role','first_name', 'last_name', 'manager']

