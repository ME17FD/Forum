from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .models import User
from .forms import UserForm


# Create your views here.

#mylogin

def userlogin(request):
    pass
 


def usersignup(request):
    pass

