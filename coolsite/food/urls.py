from django.urls import path
from django.conf.urls import handler404
from .views import *

urlpatterns = [
    path('', index),
    path('cats/<slug:cat>/', categories),
]
handler404 = 'food.views.pageNotFound'