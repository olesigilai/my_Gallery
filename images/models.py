from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
import datetime as dt


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 55)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
        
    
    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id=id).update(name = value)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=55)
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()

        @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
        
    def __str__(self):
        return self.name

class Image(models.Model):
    image = CloudinaryField('image')
    description = models.TextField()
    author = models.CharField(max_length=55, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=55)    
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete = models.DO_NOTHING)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
        
    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)


