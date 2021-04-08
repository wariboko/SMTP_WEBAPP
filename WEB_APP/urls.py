from django.urls import path

from . import views


urlpatterns = [
    path("smtp/", views.smtp, name="smtp")
    ]