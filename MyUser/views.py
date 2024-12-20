from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .models import User
from .forms import UserForm
from main.utils import check_post

# Create your views here.


def userlogin(request):
    user = request.user
    if request.user.is_authenticated:
        if request.method =='POST' and request.POST.get("type")=="post":
                check_post(request)
                return HttpResponseRedirect('/')
            
        return render(request,"logged.html",{"user":user})

    # If user is not authenticated, handle login form submission
    if request.method == 'POST':
        # Get username and password from the POST data
        username = request.POST.get("email")
        password = request.POST.get("password")
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            return render(request, 'logged.html', {"user":user})
        else:
            # If authentication fails, render login page with error message
            return render(request, 'login.html', {'message': 'Invalid username or password'})

    
    return render(request, 'login.html', {})
 


def usersignup(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mylogin')
        else:
            # If form is invalid, render the form again with error messages
            print(form.errors)
            return render(request, 'signup.html',)

    
    return render(request, 'signup.html')

def userlogout(request):
    logout(request)
    return redirect("mylogin")



def edit_profile(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            user.fname = request.POST.get('fname')
            user.lname = request.POST.get('lname')
            user.email = request.POST.get('email')
            user.phone = request.POST.get('phone')
            if request.FILES.get('profile_pic'):
                user.profile_pic = request.FILES.get('profile_pic')
            user.save()
            return redirect('mylogin')  # Redirect to the profile page after saving
        return render(request, 'edit_profile.html', {'user': user})
    else:
        return redirect("mylogin")