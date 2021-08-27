from django.urls import path

from .views import LoginView,NextView, ShowView

app_name = "accounts"




urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("login/next/", NextView.as_view(), name="next"),
    path("show/", ShowView.as_view(), name="show"),



]