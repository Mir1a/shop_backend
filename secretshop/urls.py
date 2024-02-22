"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from user.user.api.frontend.auth import views as auth_views
from drf_spectacular.views import (SpectacularSwaggerView,
                                   SpectacularRedocView,
                                   SpectacularAPIView)
from rest_framework_simplejwt import views
from django.urls import path, include
from django.contrib import admin
from django.conf.urls import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

api_urlpatterns = [
    path("api/", include("blacklist.urls")),
    path("api/", include("messenger.urls")),
    path("api/", include("finance.urls")),
    path("api/", include("project.urls")),
    path("api/", include("subject.urls")),
    path("api/", include("language.urls")),
    path("api/", include("blog.urls")),
    path("api/", include("exam.urls")),
    path("api/", include("user.urls")),
    path("api/", include("faq.urls")),
    path("api/", include("geo.urls")),
    path("api/", include("seo.urls"))
]

auth_urlpatterns = [
    path('api/frontend/token/refresh/', views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/frontend/token/', auth_views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
]

swagger_api = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

media_urlpatterns = static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += media_urlpatterns\
            + api_urlpatterns\
            + auth_urlpatterns\
            + swagger_api

if settings.DEBUG:
    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)