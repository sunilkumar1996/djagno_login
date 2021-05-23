from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from user.forms import RegisterForm, UserForgotPasswordForm

class ForgotPassword(View):
    def get(self, request):
        return render(request, "auth/change_password.html")

    def post(self, request):
        form = UserForgotPasswordForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            """
            Here the write code of send mail this code is workign progess
            """
            messages.success(request, f"Mail sent, Please check your email: {email}")
            return redirect("login")

class UserLogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.warning(request, "Logout Successfully!")
            return redirect("login")
        else:
            return redirect("login")


class UserHomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "auth/home.html")
        elif not request.user.is_authenticated:
            return redirect("login")


class LoginView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "auth/login.html")
        else:
            return redirect("home")

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Login Successfully {username}!")
                return redirect("home") 
            else:
                messages.error(request, "Your credentials is not correct!")
                return redirect("login")


class UserRegisterView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = RegisterForm()
            return render(request, "auth/register.html", {"form": form})
        else:
            return redirect("home")

    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, f"Account Created Successfully {username}!")
            return redirect("login")