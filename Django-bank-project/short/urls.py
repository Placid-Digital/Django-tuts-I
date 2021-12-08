from django.urls import path
from . import views




urlpatterns = [
    # path('', views.home, name="homepage"),
    path('register/', views.register, name="create"),
    path('login/', views.login, name="login"),
    path('profile/', views.profile, name="profile"),


]
