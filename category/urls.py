from django.urls import path
from . import views

urlpatterns = [
    path('about/<int:id>', views.aboutPage , name="about")
]
