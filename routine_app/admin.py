from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Routine

class RoutineAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'year', 'routine_file')

admin.site.register(Routine, RoutineAdmin)