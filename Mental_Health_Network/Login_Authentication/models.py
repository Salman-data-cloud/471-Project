from django.db import models
from django.contrib.auth.models import AbstractUser
from django_otp.plugins.otp_totp.models import TOTPDevice
TOTPDevice._meta.app_label = 'Login_Authentication_label'
# Create your models here.


class UserLoginAuth(AbstractUser):
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email_address'
    username = models.TextField(max_length = 20,unique = True, default = None)
    phone_number = models.CharField(max_length = 13,unique= True, blank=False)
    password = models.CharField(max_length = 8, default = None, null = True)
    email_address = models.EmailField(default =None, null = True,unique=True)

    otp_key = models.CharField(max_length= 10, blank= True, null= True)
    image = models.ImageField(upload_to = 'media/', blank = True, null = True)
    #def save(self,*args,**kwargs):

        #if not self.totpdevice_set.exists():
            #TOTPDevice.objects.create(user=self, confirmed= True)

        #super().save(*args,**kwargs)
    