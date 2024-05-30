from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=300)
    userid = models.ForeignKey(User, max_length=50, on_delete=models.CASCADE)

class Image(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=300)
    source = models.ImageField(null=True, blank=True)
    userid = models.ForeignKey(User, max_length=20, on_delete=models.CASCADE)

class Imageboard(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=300)
    source = models.ImageField(null=True, blank=True)
    userid = models.ForeignKey(User, max_length=20, on_delete=models.CASCADE)
    boardid = models.ForeignKey(Board, max_length=20, on_delete=models.CASCADE)