from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import handler404
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

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
    # path('api/v1/auth/', include('djoser.urls')),  # new
    # re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'food.views.pageNotFound'
