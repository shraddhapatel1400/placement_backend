from django.db import models
from api.companyhr.models import CompanyHr

# Create your models here.
class Quiz(models.Model):
    question = models.CharField(max_length=1000, unique=True)
    company = models.ForeignKey(CompanyHr, on_delete=models.CASCADE)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    