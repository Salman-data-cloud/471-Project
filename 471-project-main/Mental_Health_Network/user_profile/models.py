from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class Profile(models.Model):

    nick_name = models.CharField(max_length = 20, default = None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_images')
    address = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.nickname 