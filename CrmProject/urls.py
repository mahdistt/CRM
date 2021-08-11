"""CrmProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from organization.views import OrganizationInfoAPI
from users import views

urlpatterns = [
    path('crm/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('user/', include('users.urls')),
    path('organization/', include('organization.urls')),
    path('quote/', include('quote.urls')),
    path('followup/', include('followup.urls')),
    path('api/', include('rest_framework.urls')),
    path('api/v1/organization-info', OrganizationInfoAPI.as_view(), name='organization-api'),
    path('api/jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
