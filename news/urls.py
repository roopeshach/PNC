from django.urls import path
from news import views
urlpatterns = [
    
    path('news/<str:slug>', views.viewNews , name="news" ),
]
