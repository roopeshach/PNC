from django.db import models
from django.utils.text import slugify 


# Create your models here.
class Department(models.Model):
    IS_ACTIVE = (
        ('T' , 'true'),
        ('F' , 'false'),
    )
    name = models.CharField(max_length=100)
    dean = models.CharField(max_length=100)
    dean_image = models.ImageField( upload_to='department/')
    header = models.CharField(max_length=254)
    content = models.TextField()
    feature_image = models.ImageField( upload_to='department/')
    is_active = models.CharField(max_length=1 , choices=IS_ACTIVE)
    
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)

    def __str__(self):
        return self.name