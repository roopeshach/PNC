from django.db import models
from category.models import Department , Program , Custom_Page

# Create your models here.
class DepartmentImage(models.Model):
    image_title = models.CharField( max_length=254)
    department = models.ForeignKey(Department,null=True , blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.department
    

class DepartmentPostImage(models.Model):
    department_name = models.ForeignKey(DepartmentImage,default=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return str(self.department_name.department)
    