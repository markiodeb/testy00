from django.db import models
import os
from testy.settings import MEDIA_ROOT
from django.core.files.storage import FileSystemStorage
# Create your models here.

class Images(models.Model):
	nombre = models.CharField(max_length=30)
	imagen = models.ImageField(upload_to='image/img')

fs = FileSystemStorage(location=os.path.join(MEDIA_ROOT,'image/static'))
class Pics(models.Model):
	nombre = models.CharField(max_length=30)
	imagen = models.ImageField(upload_to='image/img',storage=fs)

fisy = FileSystemStorage(location=os.path.join(MEDIA_ROOT,'image/media'),base_url='/media/')
class Photos(models.Model):
	nombre = models.CharField(max_length=30)
	imagen = models.ImageField(upload_to='img',storage=fisy)

class Booly(models.Model):
	bol = models.BooleanField()

class Inty(models.Model):
	inty = models.IntegerField()
