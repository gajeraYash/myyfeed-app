from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from . import forms
# Create your views here.

def index(request):
    webpage_list = Webpage.objects.order_by('name')
    name_dict = {'webpage_rec':webpage_list}
    return render(request, 'app/index.html', context=name_dict)
    
def signup(request):
    return render(request, 'app/signup.html')


def signup_form_view(request):
    form = forms.signupForm()

    if request.method == 'POST':
        form = forms.signupForm(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS")
            print("First Name: "+ form.cleaned_data['fname'])
            print("Last Name: "+ form.cleaned_data['lname'])
            print("Email: "+ form.cleaned_data['email'])



    return render(request, 'app/signupform.html', {'form':form})