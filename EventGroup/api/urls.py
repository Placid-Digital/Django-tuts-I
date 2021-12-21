from knox import views as knox_views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views
urlpatterns = [
    path('register', views.register),
    path('login', views.Login, name='login'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]


