

# Create your models here.

from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    age = models.IntegerField()
    address = models.CharField(max_length=2048)
