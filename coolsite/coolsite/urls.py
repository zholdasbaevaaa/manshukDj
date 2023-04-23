from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404
from food.views import *
from django.urls import path, include
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'food', FoodViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('food.urls')),
    path('news/', include('news.urls')),
    path('api/v1/food/', FoodAPIList.as_view()),
    path('api/v1/food/<int:pk>/', FoodAPIUpdate.as_view()),
    path('api/v1/fooddelete/<int:pk>/', FoodAPIDestroy.as_view()),
    # path('api/v1/', include(router.urls)),
    # path('api/v1/foodlist/', FoodViewSet.as_view({'get': 'list'})),
    # path('api/v1/foodlist/<int:pk>/', FoodViewSet.as_view({'put': 'update'})),
    # path('api/v1/foodlist/', FoodAPIView.as_view()),
    # path('api/v1/foodlist/<int:pk>/', FoodAPIView.as_view()),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'food.views.pageNotFound'
