from django.db import models

from Login_Authentication.models import UserLoginAuth
# Create your models here.
class Profile(models.Model):

    # user = models.OneToOneField(UserLoginAuth, on_delete=models.CASCADE)
    # id_user = pass
    # bio =
    profileimg = models.ImageField(upload_to='profile_images')
    # location =