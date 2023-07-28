from django.db import models
from django.contrib.auth.models import AbstractUser
# from .managers import CustomUserManager
# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('n','name'),
        ('a','addres'),
        ('c','contact')
    )

    USERNAME_FIELD = 'username'
    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)
# Create your models here.
