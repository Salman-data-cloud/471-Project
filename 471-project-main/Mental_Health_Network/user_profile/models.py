from django.db import models
from Login_Authentication.models import UserLoginAuth
# Create your models here.
User = UserLoginAuth()
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=100, default = '')
    Last_Name = models.CharField(max_length=100, default = '')
    id_user = models.IntegerField(default = 1)
    mobile_number = models.CharField(max_length=15, default="1234567890")
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='profile_images')
    address = models.CharField(max_length=100,blank=True)

    
    def __str__(self):
        return self.user.username 