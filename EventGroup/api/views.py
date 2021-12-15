import users
from django.contrib.auth.handlers.modwsgi import check_password
from django.contrib.auth.hashers import make_password
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer
from django.contrib.auth import login
# RegisterSerializer
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView, LoginView


# Register

def form_data(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        address = request.POST['address']
        Email_name = request.POST['Email']
        Phone_number = request.POST['Phone']
        Password = make_password(request.POST['Password'])
        if users.objects.filter(Phone_number=Phone_number).exists():
            messages = {"status": False, "massages": "phone number already exists"}


            # return redirect('/')

        elif users.objects.filter(Email_name=Email_name).exists():
            messages = {"status": False, "massages": "Email id already exists"}
            # return redirect('/')

        else:
            users.objects.create(first_name=first_name,
                                 address=address,
                                 Email_name=Email_name, Phone_number=Phone_number, Password=Password)
            messages = {"status": True, "massages": "Registration successful"}
        return Response(messages)


def Login_form(request):
    if request.method == 'POST':
        Phone_number = request.POST['Phone']
        Password = request.POST['Password']
        if users.objects.filter(Phone_number=Phone_number).exists():
            obj = users.objects.get(Phone_number=Phone_number)
            Password = obj.Password

        else:

            messages = {"status": False, "massages": "password is incorrect"}
            return Response('password incorrect')

    else:
        messages = {"status": False, "massages": "phone number is not registered"}
        return Response('phone number is not registered')

    return Response(messages)

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "users": UserSerializer(user, context=self.get_serializer_context()).data,
            # "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(LoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        users = serializer.validated_data['users']
        login(request, users)
        return super(LoginAPI, self).post(request, format=None)

        # "users": UserSerializer.validated_data
        # token = AuthToken.objects.create(user)[1]

        # "token": AuthToken.objects.create(user)[1]
