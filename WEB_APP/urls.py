from django.urls import path
from django.contrib.auth import views as auth_views

from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    
    path("", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("smtp", views.smtp, name="smtp")
    ]