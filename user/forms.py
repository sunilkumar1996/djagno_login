from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.fields import EmailField

class UserForgotPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control rounded-left", 
            "type": "email", 
            "placeholder": "Email"
            }))

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control rounded-left", 
            "type": "password", 
            "placeholder": "Password"
            }
            ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control rounded-left",
             "type": "password", "placeholder": 
             "Confirm Password"
             }
             ))
    class Meta(UserCreationForm):
        model = User
        fields = ("username", "email",)
        widgets={
            "username": forms.TextInput(attrs={"class": "form-control rounded-left", "placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"class": "form-control rounded-left", "placeholder": "Email"}),
        }


