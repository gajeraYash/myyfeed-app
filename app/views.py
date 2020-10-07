from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from app.forms import *
from app.models import *
# Create your views here.


def index(request):
    return render(request, 'app/index.html')


def signup(request):
    registered = False
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileDOBForm(request.POST)
        data = profile_form.cleaned_data['date_of_birth']
        print(data)
        if user_form.is_valid() and profile_form.is_valid():
            userGroup = Group.objects.get(name='SiteUser')
            user = user_form.save()
            userGroup.user_set.add(user)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
    else:
        user_form = SignUpForm()
        profile_form = UserProfileDOBForm()
    return render(request, 'app/signup.html', {'user_form': user_form,
                                               'profile_form': profile_form,
                                               'registered': registered})


def signupForm(request):
    message = ''
    registered = False
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileDOBForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            message = "Error: Submitting Request"
    else:
        user_form = SignUpForm()
        profile_form = UserProfileDOBForm()
    return render(request, 'app/signupForm.html', {'user_form': user_form,
                                                   'profile_form': profile_form,
                                                   'registered': registered,
                                                   'message': message})


def user_login(request):
    
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            print("Error: Submitting Request")
    else:
        login_form = UserLoginForm()
    
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request,"app/login.html", {'login_form':login_form})
    


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def user_feed(request):
    return render(request,'app/feed.html',{})