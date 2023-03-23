from django.db import models

# Create your models here.

class CompanyHr(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254) 
    companyname = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/company/',blank=True, null=True)
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)

    status = models.IntegerField(default=-1)
    criteria = models.IntegerField(default=0)
    
    session_token = models.CharField(max_length=10, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.fullname
    