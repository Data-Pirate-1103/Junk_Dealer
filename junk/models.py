from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

# Create your models here.
class Dealer(models.Model):
    user = models.CharField(max_length=200)
    email = models.TextField(blank=True)
    ph_number = models.IntegerField()
    message = models.TextField(blank=True)
    def __str__(self):
        return self.user + '' + self.email 
  
class Contact(models.Model):
    user = models.CharField(max_length=200)
    email = models.TextField(blank=True)
    subject = models.CharField(max_length=100)
    def __str__(self):
        return self.user
