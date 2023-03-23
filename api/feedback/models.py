from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    subject = models.CharField(max_length=254) 
    message = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=254)
    image = models.ImageField(upload_to='images/technology/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    