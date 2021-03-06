from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","username","password1","password2"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control form-label"}),
            "username": forms.TextInput(attrs={"class": "form-control form-label"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control form-label"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control form-label" }),
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-label","placeholder":"Enter Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control","placeholder":"Enter Password"}))

