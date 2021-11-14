from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('download',views.download),
    path('upload/',views.upload),
]