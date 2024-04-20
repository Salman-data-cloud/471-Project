from django.db import models
from django.contrib.auth.models import AbstractUser


class UserLoginAuth(AbstractUser):
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email_address'
    username = models.TextField(max_length = 20,unique = True, default = None)
    phone_number = models.CharField(max_length = 13,unique= True, blank=False)
    password = models.CharField(max_length = 8, default = None, null = True)
    email_address = models.EmailField(default =None, null = True,unique=True)
    