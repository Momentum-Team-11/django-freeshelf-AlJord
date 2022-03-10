from multiprocessing import AuthenticationError
from urllib.error import URLError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from datetime import datetime


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Group(models.Model):
    name=models.CharField(max_length=50)
    slug= models.SlugField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Group name={self.name}>"

    def save(self):
        self.slug = slugify(self.name)
        super().save()

class Book(models.Model):
    title=models.CharField(max_length=100, null=True, blank=True)
    author=models.CharField(max_length=100, null=True, blank=True)
    description=models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.ManyToManyField(Group, related_name='book')
    favorite= models.ManyToManyField(User, name='favorite_books', blank = True)


    def __str__(self):
        return self.title




##class Genre(BaseModel):
##  name = models.Charfield
##slug = mo