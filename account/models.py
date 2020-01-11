from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    location = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=300 ,blank=True)
    company = models.CharField(max_length=100,blank=True)
    github = models.CharField(max_length=100 ,blank=True)
    linkedin = models.CharField(max_length=100 ,blank=True)
    following = models.IntegerField(default=0 ,blank=True)
    followers = models.IntegerField(default=0 ,blank=True)
    avatar = models.ImageField(upload_to='profile_images', default='profile_images/img1.png', blank=True)

    def __str__(self):
        return self.username


class Blog(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    followers = models.IntegerField(default=0 ,blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    avatar = models.ImageField(upload_to='profile_images', default='blog_mages/img1.png', blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return "{} by {}".format(self.title, self.user.username)







