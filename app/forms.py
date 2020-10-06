from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from app.models import UserProfile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    username = forms.CharField(max_length=15, min_length=3, required=True, help_text="Username can must be between 3 - 15 characters and can contain '_'. ",validators=[
        RegexValidator(
            regex='^(?=.{3,15}$)(?!.*[_]{2})[a-zA-Z0-9_]+$',
            message='Username is invalid!',
            code='invalid_username'
        ),
    ])
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control','aria-describedby':'basic-addon1'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already in use.")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already in use.")
        return self.cleaned_data

    
class UserProfileDOBForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('date_of_birth',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs.update({'class': 'form-control','type':"date"})


class UserProfileDetailForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic','user_bio','user_location')
