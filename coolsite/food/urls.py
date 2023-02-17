from django.urls import path
from django.conf.urls import handler404

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('main', views.about, name='main'),
]
handler404 = 'food.views.pageNotFound'