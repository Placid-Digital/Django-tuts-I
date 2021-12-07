from django.urls import path
from django.contrib import admin

 


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
    
]