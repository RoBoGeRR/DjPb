from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields = ['username', 'email', 'password']

class UserProfileRegistrationForm(forms.ModelForm):
    class Meta: 
        model = UserProfile
        fields=['profile_picture']