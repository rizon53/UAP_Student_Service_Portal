from django.db import models

# Create your models here.
from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    room = models.CharField(max_length=50, blank=True)
    department = models.ForeignKey('departments.Department', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
