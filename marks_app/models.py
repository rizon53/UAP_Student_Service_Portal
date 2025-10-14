from django.db import models
from django.contrib.auth.models import User

class Marks(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    ct1 = models.FloatField(default=0)
    ct2 = models.FloatField(default=0)
    ct3 = models.FloatField(default=0)
    mid = models.FloatField(default=0)
    final = models.FloatField(default=0)

    def __str__(self):
        return f"{self.student.username} - {self.subject}"