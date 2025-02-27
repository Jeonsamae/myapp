from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    occupation = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
