from django.db import models
from django.contrib.auth.models import User

class Library(models.Model):
     title = models.CharField(max_length=255)
     user = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
          return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    youtube_id = models.CharField(max_length=255)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

