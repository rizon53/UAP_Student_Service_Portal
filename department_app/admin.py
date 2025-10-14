from django.contrib import admin
from .models import DepartmentContact

@admin.register(DepartmentContact)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')