from django.shortcuts import render
from news.models import News
from category.models import Department, Program , Custom_Page
from home.models import Content
# Create your views here.


content = Content.objects.all().first()
departments = Department.objects.all().filter(is_active="T")
programs = Program.objects.all().filter(is_active="T")
pages = Custom_Page.objects.all().filter(is_active="T")


def viewNews(request, slug):
    news = News.objects.get(slug=slug)
    context_news = {
        'content' : content,
        'departments' : departments,
        'programs' : programs,
        'pages' : pages,
        'news':news,


    }
    return render(request , 'news/news.html' , context_news)