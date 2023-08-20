from django.db import models


class Importer(models.Model):
    user_name = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100,blank=False, null=False)
    email     = models.EmailField(unique=True)
    address   = models.TextField(max_length=300, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='Importer')

# Create your models here.
