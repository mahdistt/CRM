from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.show_base, name='show-base'),

]
