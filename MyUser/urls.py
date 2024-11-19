
from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [

    path('', views.userlogin , name = "mylogin"),
    path('signup/', views.usersignup , name = "signup"),
    path('logout/', views.userlogin , name = "logout"),
     

]