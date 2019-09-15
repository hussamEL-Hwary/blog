from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100)
    category_slug = models.CharField(max_length=200, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    min_read = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
    comments = models.IntegerField(default=0)
    img_url = models.CharField(max_length=250 ,null=True)

    def commented(self):
        self.comments += 1
        self.save(update_fields=['comments'])

    def __str__(self):
        return self.title

class Message(models.Model):
    author = models.CharField(max_length=60, default="visitor")
    email = models.CharField(max_length=120)
    body = models.TextField()

    def __str__(self):
        return self.author

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class VisitorInfo(models.Model):
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    lat = models.CharField(max_length=60)
    longt = models.CharField(max_length=60)
    ip = models.CharField(max_length=60)

    def __str__(self):
        return self.ip
