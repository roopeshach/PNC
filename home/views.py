from django.shortcuts import render
from .models import Content , Slider , Description

# Create your views here.
content = Content.objects.all().first()
desc = Description.objects.all().first()
slides = Slider.objects.all()
context = {
    'content' : content,
    'slides' : slides,
    'desc' : desc,
}
def header(request):
    return render(request, 'home/index.html', context)

def index(request):
    return render(request , 'home/index.html')

