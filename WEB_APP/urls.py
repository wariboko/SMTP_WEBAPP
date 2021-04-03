from django.urls import path

from . import views

app_name = "SMTP_WEBAPP"
urlpatterns = [
    path("SMTP_WEBAPP/index/", views.index, name="index")
    ]