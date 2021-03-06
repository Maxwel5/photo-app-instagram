from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    photo = models.ImageField(blank=True)
    bio = models.CharField(max_length =120)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.update()

    def delete_profile(self):
        self.delete()

    class Meta:
        ordering = ['photo']

class Image(models.Model):
    image_image = models.ImageField(upload_to='images/' , default = 'images/default.jpeg')
    name = models.CharField(max_length = 100)
    caption = models.CharField(max_length = 150)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name= 'likes', blank = True)
    comments = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def total_likes(self):
        self.likes.count()

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def update_caption_image(self):
        self.update_caption()

    def delete_image(self):
        self.delete()

    def tearDown(self):
        Profile.objects.all().delete()
        instagram.objects.all().delete()
        Image.objects.all().delete()

    @classmethod
    def search_by_name(cls,search_term):
        instagram = cls.objects.filter(name__icontains=search_term)
        return instagram

class Instagram(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    comments = models.TextField()
    image = models.ForeignKey(Image,on_delete=models.PROTECT, related_name='image_comments',default=1)

    def __str__(self):
        return self.comments

    def save_comments(self):
        self.save()

    def delete_comments(self):
        self.delete()



