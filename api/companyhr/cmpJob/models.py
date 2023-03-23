from django.db import models

from api.companyhr.models import CompanyHr
# Create your models here.

class CompanyJob(models.Model):
    company = models.ForeignKey(CompanyHr, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=50)
    vacancy = models.CharField(max_length=10)
    jobtype = models.CharField(max_length=20) 
    deadline = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.requirement
    