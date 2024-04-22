from django.db import models
from Login_Authentication.models import UserLoginAuth
# Create your models here.
User = UserLoginAuth()
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images')
    location = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username