from django.db import models

# Create your models here.

class Profile(models.Model):
    photo = models.ImageField(blank=True)
    bio = models.TextField()

class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length = 100)
    caption = models.CharField(max_length = 150)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)
    comments = models.TextField()

class Instagram(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()

