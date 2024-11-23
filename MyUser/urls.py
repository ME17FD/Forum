
from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [

    path('', views.userlogin , name = "mylogin"),
    path('signup/', views.usersignup , name = "signup"),
    path('logout/', views.userlogout , name = "logout"),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
     

]