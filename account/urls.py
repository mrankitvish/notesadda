
from . import views
from django.urls import path

urlpatterns=[
    path('signup/',views.usignup),
    path('login/',views.ulogin),
    path('logout/',views.ulogout),]
   