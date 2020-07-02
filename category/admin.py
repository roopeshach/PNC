from django.contrib import admin
from .models import Department , Program
# Register your models here.
class department(admin.ModelAdmin):
    list_display  = ['name' , 'dean' , 'header']

class program(admin.ModelAdmin):
    list_display  = ['name' , 'dean' , 'header']
    
admin.site.register(Department, department)
admin.site.register(Program , program)
