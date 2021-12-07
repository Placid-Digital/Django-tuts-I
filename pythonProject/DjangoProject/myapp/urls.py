from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.home,name='home'),
    path('sing_up/',views.sing_up,name='singup'),
    path('login/',views.form,name='form'),
    path('form_data/', views.Login_form, name='form'),
    path('web/',views.web_page,name='web'),
    path('data/',views.data_page,name='data')




    ]