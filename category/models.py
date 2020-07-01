from django.db import models

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
    
    