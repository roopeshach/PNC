from django.contrib import admin
from .models import Department
# Register your models here.
class department(admin.ModelAdmin):
    list_display  = ['name' , 'dean' , 'header']
admin.site.register(Department, department)