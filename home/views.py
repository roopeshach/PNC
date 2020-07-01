from django.shortcuts import render
from .models import Content , Slider , Description
from category.models import Department

# Create your views here.
content = Content.objects.all().first()
desc = Description.objects.all().first()
slides = Slider.objects.all()
departments = Department.objects.all().filter(is_active="T")

context = {
    'content' : content,
    'departments' : departments,
    'slides' : slides,
    'desc' : desc,

}

def index(request):
    return render(request , 'home/index.html', context)

