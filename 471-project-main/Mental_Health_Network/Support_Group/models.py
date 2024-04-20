from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class SupportGroup(models.Model):
    name = models.CharField(max_length = 200, unique= True)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    support_group = models.ForeignKey(SupportGroup, on_delete = models.CASCADE)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.user.username} : {self.message}'
    
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete= models.CASCADE)
    support_group = models.ForeignKey(SupportGroup, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username
    
