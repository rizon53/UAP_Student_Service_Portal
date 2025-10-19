from django.db import models

class Feedback(models.Model):
    message = models.TextField()

    def __str__(self):
        return self.message[:30]