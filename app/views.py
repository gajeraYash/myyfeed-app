
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from app.forms import *
from app.models import *
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/feed')
    else:
        return render(request, 'app/index.html')
    

@login_required
def user_feed(request):
    profile_data = UserProfile.objects.get(user=request.user)
    return render(request,'app/feed.html',{"profile_data":profile_data})

def user_signup_success(request):
    registered = True
    return render(request,'app/signup.html',{'registered': registered})

def user_signup(request):
    message = ''
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileDOBForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect('/signup/success')
        else:
            message = "Error: Submitting Request"
    else:
        user_form = SignUpForm()
        profile_form = UserProfileDOBForm()
    return render(request, 'app/signup.html', {'user_form': user_form,
                                                   'profile_form': profile_form,
                                                   'message': message})


def user_login(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request,user)
            return HttpResponseRedirect("/feed")
        else:
            print("Error: Submitting Request")
    else:
        login_form = UserLoginForm()
    
    if request.user.is_authenticated:
        return HttpResponseRedirect('/feed')
    else:
        return render(request,"app/login.html", {'login_form':login_form})
    

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
