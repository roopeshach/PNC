from django.db import models
from category.models import Department , Program
from tinymce import HTMLField
from django.utils.text import slugify
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=254)
    content = HTMLField()
    date = models.DateTimeField()
    image = models.ImageField( upload_to="events/")

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField( max_length=254)
    content = HTMLField()
    date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True,default=0, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True,default=0,blank=True)
    image = models.ImageField( upload_to="news/", null=True , blank=True)
    file = models.FileField( upload_to="news_file/" , blank=True , null=True)

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Notice(models.Model):
    title = models.CharField( max_length=254)
    content = HTMLField()
    date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True,default=0, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True,default=0,blank=True)
    image = models.ImageField( upload_to="notice/" , null=True , blank=True)
    file = models.FileField( upload_to="notice_file/" , blank=True , null=True)

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Notice, self).save(*args, **kwargs)

    def __str__(self):
        return self.title