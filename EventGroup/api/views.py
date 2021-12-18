import users
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from knox.views import LoginView
from rest_framework import generics
# RegisterSerializer
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Users
from .serializers import UserSerializer


# Register API
@csrf_exempt
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        first_name = request.data['name']
        Email_name = request.data['email']
        Phone_number = request.data['phone']
        address = request.data['address']
        Password = make_password(request.data['password'])
        # data = UserSerializer(data=request.data)
        # if data.is_valid():

        if Users.objects.filter(phone_no=Phone_number).exists():
            messages = {"status": False, "massage": "phone number already exists"}


        elif Users.objects.filter(email=Email_name).exists():
            messages = {"status": False, "massage": "Email id already exists"}

        else:
            Users.objects.create(first_name=first_name,
                                 address=address,
                                 email=Email_name,
                                 phone_no=Phone_number,
                                 password=Password)
            messages = {"status": True, "massage": "Registration successful"}
        return Response(messages)

    def get(self, request):
        return Response({"Hello world"})

# LOGIN API
@csrf_exempt
@api_view(['POST'])
def Login(request):
    if request.method == 'POST':
        Phone_number = request.data['phone']
        Users_Password = request.data['password']
        if Users.objects.filter(phone_no=Phone_number).exists():
            obj = Users.objects.get(phone_no=Phone_number)
            password = Users_Password

            if check_password(Users_Password, password):
                messages = {'status': True, 'massage': 'login successful'}

            else:

                messages = {"status": False, "massage": "password is incorrect"}
                # return Response('password incorrect')

        else:
            messages = {"status": False, "massage": "phone number is not registered"}
            # return Response('phone number is not registered')
        #
        return Response(messages)


