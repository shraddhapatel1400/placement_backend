from django.db import models
from api.student.models import Student

# Create your models here.

class Education(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    board = models.CharField(max_length=254) 
    yearofpassing = models.IntegerField() 
    ogpa = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course