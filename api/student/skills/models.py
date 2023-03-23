from django.db import models
from api.student.models import Student

# Create your models here.

class Skills(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    level = models.CharField(max_length=100) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.skill