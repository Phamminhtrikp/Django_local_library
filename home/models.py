from django.db import models

# Create your models here.
class myblog(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    quantity=models.IntegerField()
    image=models.CharField(max_length=255)


# User models
class Users(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    status = models.CharField(max_length=30)


