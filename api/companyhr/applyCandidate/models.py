from django.db import models

from api.companyhr.cmpJob.models import CompanyJob
from api.student.models import Student

# Create your models here.
class ApplyJob(models.Model):
    job = models.ForeignKey(CompanyJob, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    body = models.CharField(max_length=1000,blank=True, null=True)
    resume = models.FileField(upload_to='resume/',blank=True, null=True)
    applydate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.body
    