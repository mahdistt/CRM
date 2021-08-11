from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.show_dashboard, name='dashboard'),
    # path('add/', views.show_register_organization_form, name='add'),
    path('create/', views.CreateFormOrganization.as_view(), name='create'),
    # path('org/<int:pk>', views.ViewPost.as_view(), name='detail'),

]
