from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('analysis/<int:file_id>/', views.data_analysis, name='data_analysis'),
]

