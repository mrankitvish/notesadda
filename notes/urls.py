from django.urls import path
from . import views

urlpatterns=[
    path('download/',views.FileView.as_view(), name='files'),
    path('upload/',views.uploadFile,name='upload'),
    
]