from django.urls import path
from . import views

app_name = "shadi"






urlpatterns = [
    path("register/", views.register_request, name="register"),
    path('data/', views.data, name='alldata'),
    path('delete_user/', views.delete_user),
    path('update_view/<int:uid>/', views.update_view),
    path('update_form_data/', views.update_form_data, ),

]