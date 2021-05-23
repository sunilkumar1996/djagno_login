from django.urls import path
from user import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name="login"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("", views.UserHomeView.as_view(), name="home"),
]
