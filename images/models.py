from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
import datetime as dt


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 55)
    

