from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",view=views.home,name="home"),
    path("post/<uuid:post_id>/",view=views.Specif_Post,name="spost"),
    path("Bookmark/",view=views.Bookmark,name="bookmark"),


]
