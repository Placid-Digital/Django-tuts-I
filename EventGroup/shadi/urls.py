from django.urls import path
from . import views

app_name = "shadi"






urlpatterns = [
    # path("", views.homepage, name="homepage"),
    path("registeration", views.register_request, name="register"),
    path("login", views.login_request, name="login")
]