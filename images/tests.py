from django.test import TestCase
from .models import Location,Image,Category
import datetime as dt
# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location = Location(id=1,name = 'Prestige')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
        
    # Testing Save Method
    def test_save_method(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
# Testing delete Method
    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location)== 0) 
        # Testing update location Method
    def test_update_location(self):
        self.location.save_location()
        self.location.update_location(self.location.id, 'Karen')
        changed_location = Location.objects.filter(name ='Karen')
        self.assertTrue(len(changed_location) > 0) 
class ImageTestClass(TestCase):
    def setUp(self):
    # Creating a new location and saving it
        self.location = Location(id=1,name = 'Prestige')
        self.location.save_location()

        # Creating a new category and saving it
        self.category = Category(id=1,name = 'study')
        self.category.save_category()

        self.new_image= Image(id=1, name='image', description='this is a test image', location=self.location,category=self.category)
        self.new_image.save()

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
         # Testing Save Method
    def test_save_method(self):
        self.new_image.save_image()
        new_image = Image.objects.all()      
        self.assertTrue(len(new_image) >0)
        #testing delete function
    def test_delete_image(self):
        self.new_image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image)== 0)
        #testing image update method
    def test_update_image(self):
        self.new_image.save_image()
        self.new_image.update_image(self.new_image.id, 'images/giidi.jpg')
        changed_img = Image.objects.filter(image='images/giidi.jpg')
        self.assertTrue(len(changed_img) > 0)
        
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.category = Category(id=1,name = 'study')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))
        
    # Testing Save Method
    def test_save_method(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)
        #testing delete function
    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category)== 0)
        #testing update method
    def test_update_category(self):
        self.category.save_category()
        self.category.update_category(self.category.id, 'Football')
        changed_category = Category.objects.filter(name ='Football')
        self.assertTrue(len(changed_category) > 0)
    
    def tearDown(self):
            Location.objects.all().delete()
            Category.objects.all().delete()
            Image.objects.all().delete()