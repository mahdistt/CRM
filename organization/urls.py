from django.urls import path
from . import views
app_name = 'organization'
urlpatterns = [
    path('org/<int:pk>', views.ViewOrganization.as_view(), name='detail'),
]
