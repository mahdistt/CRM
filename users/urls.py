from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('lagin/', views.AdminLoginView.as_view(), name='login'),
    path('logout/', views.AdminLogoutView.as_view(), name='logout'),
    path('admin/profile', views.EditProfile.as_view(), name='edit_profile'),

]
