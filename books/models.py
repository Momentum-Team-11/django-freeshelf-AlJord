from multiprocessing import AuthenticationError
from urllib.error import URLError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title=models.CharField(max_length=100, null=True, blank=True)
    author=models.CharField(max_length=100, null=True, blank=True)
    description=models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    URL=models.URLField(max_length=100,null=True, blank=True)


    def __str__(self):
        return self.title




##class Genre(BaseModel):
 ##  name = models.Charfield
 ##slug = mo