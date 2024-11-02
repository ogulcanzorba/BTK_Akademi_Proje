from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.home, name='home'),
    path('home/<slug:lecture_name>/', views.lecture_detail, name='lecture_detail'),
]