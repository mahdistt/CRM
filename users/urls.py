from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('', views.AdminLoginView.as_view(), name='login'),
    path('logout/', views.AdminLogoutView.as_view(), name='logout'),
]
