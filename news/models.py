from django.db import models
from category.models import Department , Program
from tinymce import HTMLField
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=254)
    content = HTMLField()
    date = models.DateTimeField()
    image = models.ImageField( upload_to="events/")


class News(models.Model):
    title = models.CharField( max_length=254)
    content = HTMLField()
    date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True,default=0, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True,default=0,blank=True)
    image = models.ImageField( upload_to="news/", null=True , blank=True)
    file = models.FileField( upload_to="news_file/" , blank=True , null=True)

class Notice(models.Model):
    title = models.CharField( max_length=254)
    content = HTMLField()
    date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True,default=0, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True,default=0,blank=True)
    image = models.ImageField( upload_to="notice/" , null=True , blank=True)
    file = models.FileField( upload_to="notice_file/" , blank=True , null=True)