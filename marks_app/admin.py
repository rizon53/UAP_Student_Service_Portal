from django.contrib import admin
from .models import Marks

class MarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'ct1', 'ct2', 'ct3', 'mid', 'final']

admin.site.register(Marks, MarksAdmin)