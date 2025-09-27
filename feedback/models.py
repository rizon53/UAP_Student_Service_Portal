from django.db import models

# Create your models here.
from django.db import models

class Feedback(models.Model):
    text = models.TextField()
    anonymous = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback #{self.id} ({'anon' if self.anonymous else 'named'})"
