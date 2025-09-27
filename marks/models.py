from django.db import models

# Create your models here.
from django.db import models

class Mark(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    EXAM_TYPES = (('CT', 'CT'), ('Exam', 'Exam'))
    exam_type = models.CharField(max_length=10, choices=EXAM_TYPES, default='CT')
    marks = models.DecimalField(max_digits=6, decimal_places=2)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.student_id} - {self.subject}: {self.marks}"
