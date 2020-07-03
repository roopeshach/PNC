from django.shortcuts import render
from news.models import News , Notice
from category.models import Department, Program , Custom_Page
from home.models import Content
from django.core.paginator import Paginator ,  EmptyPage, PageNotAnInteger
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

def allNews(request):

    news_list = News.objects.all()


    page = request.GET.get('page', 1)    
    paginator = Paginator(news_list, 8)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)


    context = {
        'content' : content,
        'departments' : departments,
        'programs' : programs,
        'pages' : pages,
        'news' : news,
    }
    print(news)
    return render(request , 'news/allnews.html', context)


def allNotice(request):

    notice_list = Notice.objects.all()


    page = request.GET.get('page', 1)    
    paginator = Paginator(notice_list, 8)
    try:
        notice = paginator.page(page)
    except PageNotAnInteger:
        notice = paginator.page(1)
    except EmptyPage:
        notice = paginator.page(paginator.num_pages)


    context = {
        'content' : content,
        'departments' : departments,
        'programs' : programs,
        'pages' : pages,
        'notice' : notice,
    }
    print(notice)
    return render(request , 'news/allnotice.html', context)