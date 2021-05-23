from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages


class UserHomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "auth/home.html")
        elif not request.user.is_authenticated:
            return redirect("login")

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "auth/login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages(request, f"Login Successfully {username}!")
                return redirect("home") 
            else:
                messages.error(request, "Your credentials is not correct!")
                return redirect("login")


class UserRegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "auth/register.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, f"Account Created Successfully {username}!")
            return redirect("login")