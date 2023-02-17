from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404
from food.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food.urls')),
    path('news/', include('news.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'food.views.pageNotFound'
# handler400 = acccesDenied
# handler500 = serverError
# handler403 = forbidden