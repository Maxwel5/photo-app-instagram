from django.db import models

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.bio

    class Meta:
        ordering = ['photo', 'bio']

class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length = 100)
    caption = models.CharField(max_length = 150)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)
    comments = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Instagram(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()

