from django.urls import path
from django.contrib import admin
from knox import views as knox_views



from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.home,name='home'),
    path('formdata/',views.form_data,name='form'),
    path('login/',views.login_page,name='form'),
    path('login_data/',views.Login_form,name='form'),
    path('welcome/',views.welcome_page,name='view'),
    path('data/',views.data,name='alldata'),
    path('delete_user/', views.delete_user),
    path('update_view/<int:uid>/',views.update_view),
    path('update_form_data/',views.update_form_data,),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),


    
]