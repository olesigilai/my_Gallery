from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
import datetime as dt


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 55)

    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id=id).update(name = value)
    def __str__(self):
        return self.name

