
from django.contrib import admin
from django.urls import path

from food.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food.urls')),
]

handler404 = pageNotFound
# handler400 = acccesDenied
# handler500 = serverError