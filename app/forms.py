from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from app.models import UserProfile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already in use")
        elif User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
        return self.cleaned_data
        


class UserProfileDOBForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('date_of_birth',)

        

class UserProfileDetailForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic','user_bio','user_location')
