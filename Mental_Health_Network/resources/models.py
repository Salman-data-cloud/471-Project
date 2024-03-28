from django.db import models

# Create your models here.


class Book(models.Model):
    #id = models.AutoField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image  = models.ImageField(upload_to ="resources/files/covers")
    url = models.URLField()


class Article(models.Model):
    #id = models.AutoField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image  = models.ImageField(upload_to="resources/files/covers")
    url = models.URLField()


class Podcast(models.Model):
    title = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    description = models.TextField()
    image  = models.ImageField(upload_to="resources/files/covers")
    url = models.URLField()

