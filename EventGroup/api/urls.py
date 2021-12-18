from django.urls import path
from knox import views as knox_views
from django.urls import path
from . import views
urlpatterns = [
    path('register', views.register),
    path('login', views.Login, name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]