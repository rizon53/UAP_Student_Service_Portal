from django.contrib.auth.models import User
from django.db import models

class FacultyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
