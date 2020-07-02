from django.shortcuts import render
from .models import Department , Program
from home.models import Content

# Create your views here.

def aboutDepartment(request, slug):
    content = Content.objects.all().first()
    departments = Department.objects.all().filter(is_active="T")
    programs = Program.objects.all().filter(is_active="T")
    dept = Department.objects.get(slug=slug)
    

    context = {
    'content' : content,
    'departments' : departments,
    'dept':dept,
    'programs' : programs
    
    }
    return render(request, 'category/about.html' , context)

def aboutProgram(request, slug):
    content = Content.objects.all().first()
    departments = Department.objects.all().filter(is_active="T")
    programs = Program.objects.all().filter(is_active="T")
    program = Program.objects.get(slug=slug)
    context_program = {
        'content' : content,
        'departments' : departments,
        'program' : program,
        'programs' : programs
    }

    return render(request , 'category/aboutProgram.html' , context_program)