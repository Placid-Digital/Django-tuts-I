from django.urls import path
from . import views

app_name = "shadi"






urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.home, name='home'),
    path("registeration", views.register_request, name="register"),
    path("login", views.login_request, name="login")
]