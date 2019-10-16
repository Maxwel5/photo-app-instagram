from django.db import models
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.update()

    def delete_profile(self):
        self.delete()

    class Meta:
        ordering = ['photo', 'bio']

class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length = 100)
    caption = models.CharField(max_length = 150)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)
    comments = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

class Instagram(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()

