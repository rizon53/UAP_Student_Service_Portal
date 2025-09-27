from django.db import models

# Create your models here.
from django.db import models

class Routine(models.Model):
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()
    file = models.FileField(upload_to='routines/')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('department', 'year')

    def __str__(self):
        return f"Routine {self.department.code} Y{self.year}"
