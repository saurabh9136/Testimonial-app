from django.db import models

# Create your models here.

class Emp(models.Model) :
    name = models.CharField(max_length=25)
    emp_id = models.CharField(max_length=5)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=256)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=20)

class Feedback(models.Model):
    email = models.EmailField( max_length=254)
    name = models.CharField(max_length=50)
    feed = models.TextField()

    
    
