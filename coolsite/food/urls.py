from django.urls import path
from django.conf.urls import handler404

from . import views
from .views import *


urlpatterns = [
    path('', FoodHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', FoodCategory.as_view(), name='category'),
]
# handler404 = 'food.views.pageNotFound'
