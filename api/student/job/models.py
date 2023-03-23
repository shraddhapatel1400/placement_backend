from django.db import models
from api.student.models import Student

# Create your models here.

class Summary(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    experience = models.CharField(max_length=100) 
    objective = models.CharField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position