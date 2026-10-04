from django.urls import path
from .views import register , login_view , home , logout_view

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout_view"),
    path("", home, name="home"),
]