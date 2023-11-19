from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    gender = models.CharField(max_length=5)
    
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')