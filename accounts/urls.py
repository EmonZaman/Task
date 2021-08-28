from django.urls import path

from .views import LoginView, ShowView

app_name = "accounts"

urlpatterns = [
    path('', LoginView.as_view(), name="register"),

    path('login/', ShowView.as_view(), name="login"),

]
