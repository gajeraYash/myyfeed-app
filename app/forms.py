from django import forms

class signupForm(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()
    email = forms.EmailField()