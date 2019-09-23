from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Video(models.Model):
    url = models.URLField()


class Problem(models.Model):
    condition = models.CharField(max_length=500)
    solution = models.CharField(max_length=1000)


class Post(models.Model):
    name = models.CharField(max_length=150, )
    videos = models.ForeignKey(Video, on_delete=models.CASCADE)
    problems = models.ForeignKey(Problem, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
