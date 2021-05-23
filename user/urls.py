from django.urls import path
from django.views.generic.base import View
from user import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login', views.LoginView.as_view(), name="login"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
    # path("logout/", login_required(views.UserLogoutView.as_view()), name="logout"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("", views.UserHomeView.as_view(), name="home"),
]
