from django.urls import path

from . import views

app_name = 'quote'
urlpatterns = [
    path('create/', views.QuoteCreateView.as_view(), name='create-quote'),
    path('list/', views.QuoteListView.as_view(), name='list-quote'),
    path('detail/<int:pk>', views.QuoteDetailView.as_view(), name='detail-quote'),
    path('print/<int:pk>', views.QuotePDFView.as_view(), name='pdf-quote'),
]
