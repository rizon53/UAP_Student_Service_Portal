from django.db import models

# Create your models here.
from django.db import models

# Add all UAP departments
DEPARTMENTS = [
    ('CSE', 'Computer Science & Engineering'),
    ('EEE', 'Electrical & Electronic Engineering'),
    ('Civil', 'Civil Engineering'),
    ('Architecture', 'Architecture'),
    ('BBA', 'Business Administration'),
    ('Law', 'Law'),
    ('English', 'English'),
    ('Economics', 'Economics'),
    # Add more departments if needed
]

YEARS = [
    ('1.1', '1.1'),
    ('1.2', '1.2'),
    ('2.1', '2.1'),
    ('2.2', '2.2'),
    ('3.1', '3.1'),
    ('3.2', '3.2'),
    ('4.1', '4.1'),
    ('4.2', '4.2'),
]


class Routine(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=50, choices=DEPARTMENTS, default='CSE')
    year = models.CharField(max_length=10, choices=YEARS, default='1.1')
    routine_file = models.FileField(upload_to='routines/', blank=True, null=True)  # ✅ nullable

    def __str__(self):
        return f"{self.department} {self.year} - {self.title or 'Routine'}"