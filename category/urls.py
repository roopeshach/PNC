from django.urls import path
from . import views

urlpatterns = [
    path('about/<str:slug>', views.aboutPage , name="about")
]
