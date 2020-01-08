from django.db import models
import datetime as dt
# Create your models here.

class Profile(models.Model):
    title = models.CharField(max_length =30)
    Bio = models.TextField(max_length = 150, blank=True)

    def __str__(self):
        return self.title

    def save_profile(self):
        self.save()

class Post(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    profile = models.ForeignKey(Profile)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'posts/')

    @classmethod
    def search_by_title(cls,search_term):
        gram = cls.objects.filter(title__icontains=search_term)
        return gram

class PostForm(models.Model):
    caption = models.CharField(max_length = 50)
    image = models.ImageField()
    