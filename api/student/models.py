from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254) 
    image = models.ImageField(upload_to='images/student/',blank=True, null=True)
    address = models.CharField(max_length=254,blank=True, null=True)
    phone = models.CharField(max_length=13,blank=True, null=True)
    
    pdf = models.FileField(upload_to='images/student/',blank=True, null=True)

    status = models.IntegerField(default=-1)

    session_token = models.CharField(max_length=10, default=0)

    last_login = models.DateTimeField(auto_now=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.firstname + ' ' + self.lastname
    