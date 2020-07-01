from django.shortcuts import render
from .models import Department
from home.models import Content
from home import views
# Create your views here.

def aboutPage(request, slug):
    content = Content.objects.all().first()
    departments = Department.objects.all().filter(is_active="T")
    dept = Department.objects.get(slug=slug)

    context = {
    'content' : content,
    'departments' : departments,
    'dept':dept,
    }
    return render(request, 'category/about.html' , context)