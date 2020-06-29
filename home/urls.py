from home import views
from django.urls import path

urlpatterns = [
    path('',views.header , name="header"),
    path('', views.index, name="index")
]


