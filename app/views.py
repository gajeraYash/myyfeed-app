from django.contrib.auth.models import Group
from django.shortcuts import render
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
        if user_form.is_valid() and profile_form.is_valid():
            userGroup = Group.objects.get(name='SiteUser')
            user = user_form.save()
            userGroup.user_set.add(user)
            user.save()
            profile = profile_form.save(commit= False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = SignUpForm()
        profile_form = UserProfileDOBForm()
    return render(request, 'app/signup.html', {'user_form': user_form, 
                                                'profile_form':profile_form,
                                                'registered':registered})

def signupForm(request):
    registered = False
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileDOBForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            userGroup = Group.objects.get(name='SiteUser')
            user = user_form.save()
            userGroup.user_set.add(user)
            user.save()
            profile = profile_form.save(commit= False)
            profile.user = user
            profile.save()
            registered = True
        else:
            message = "Error: Submitting Request"
    else:
        user_form = SignUpForm()
        profile_form = UserProfileDOBForm()
    return render(request, 'app/signupForm.html', {'user_form' : user_form, 
                                                'profile_form' : profile_form,
                                                'registered' : registered})
