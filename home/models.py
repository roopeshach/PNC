from django.db import models

# Create your models here.
class Content(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=254)
    contact_info = models.TextField()
    logo_img = models.ImageField(upload_to="images/")

class Slider(models.Model):
    head = models.CharField( max_length=254)
    content = models.TextField()
    photo = models.ImageField( upload_to="slider")

class Description(models.Model):
    header = models.CharField(max_length=254)
    content = models.TextField()