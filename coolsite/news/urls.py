from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('news/', views.news_home, name='news_home'),

]