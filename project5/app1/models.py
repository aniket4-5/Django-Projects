from pyexpat import model
from django.db import models
from django.forms import CharField

# Create your models here.


class Post(models.Model):
    titel = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    descripton = models.CharField(max_length=1000)
