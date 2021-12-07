from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.response import Response

from api.form import Loginform


# Create your views here.

from api.serializers import PersonSerializer, SpeciesSerializer
from api.models import Person, Species


class PersonViewSet(viewsets.ModelViewSet):
   queryset = Person.objects.all()
   serializer_class = PersonSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
   queryset = Species.objects.all()
   serializer_class = SpeciesSerializer


def LoginForm(request):
   username = "not logged in"

   if request.method == "POST":
      # Get the posted form
      MyLoginForm = Loginform(request.POST)

      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']


   else:
      MyLoginForm = Loginform()

   # return render(request, 'loggedin.html', {"username": username})


def Login_form(request):
   if request.method == 'POST':
      email_name = request.POST['email']
      User_Password = request.POST['pswd']
      if Person.objects.filter(Email_name=email_name).exists():
         obj = Person.objects.get(Email_name=email_name)
         Password = obj.Password

         if check_password(User_Password, Password):
            return Response(
               {"Status": True, "message": "Successful Login"}
            )
         else:
            # return HttpResponse('password incorrect')
            return Response(
               {"Status": False, "message": "Incorrect Password"}
            )
      else:
         # return HttpResponse('Email is not registered')
         return Response(
            {"Status": False, "message": "Email is not registered"}
         )
   else:
      # return HttpResponse('Method not allowed', status=403)
      return Response(
         {"Status": False, "message": "Method not allowed"}
      )



