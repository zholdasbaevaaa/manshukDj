from django.urls import path
from django.conf.urls import handler404
from django.views.decorators.cache import cache_page

from . import views
from .views import *


urlpatterns = [
    path('', cache_page(60)(FoodHome.as_view()), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', FoodCategory.as_view(), name='category'),
]
# handler404 = 'food.views.pageNotFound'
