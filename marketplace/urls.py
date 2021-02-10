from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .swagger_urls import doc_urls


urlpatterns = [
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/login/', include('djoser.urls')),
    path('api/v1/login/', include('djoser.urls.authtoken')),
    path('api/v1/login/', include('djoser.urls.jwt')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('api/v1/', include('api.urls_api')),
    path('admin/', admin.site.urls),
]

urlpatterns += doc_urls

    

