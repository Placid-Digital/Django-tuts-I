from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView, View
from rest_framework.response import Response

from myapp.models import Person


# Create your views here.

def view():
    render('home.html')


def home():
    return "this is my first page."


def form():
    return "this is my first page."


def form_page(request):
    return render(request, 'myapp/form.html')


def web_page(request):
    return render(request, 'myapp/web.html')


# create Table data form
def data_page(request):
    persons = Person.objects.filter(is_active=True).order_by('id')
    print(persons)
    return render(request, 'myapp/table.html',
                  context={
                      'request': request,
                      'persons': persons,
                  }
                  )

# render tamplates for home.html
def index(request):
    return render(request, 'myapp/home.html', context={})


# render tamplates for form.html
def form(request):
    return render(request, 'myapp/form.html', context={})


# render tamplates for website.html
def web(request):
    return render(request, 'myapp/web.html', context={})

# creat home view
class AboutUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")


# creat login view
class logintUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, "form.html")


# creat website view
class webUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, "web.html")


# creat table view

class dataUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, "table.html")


# creat sing_up page

def sing_up(request):
    if request.method == 'POST':
        first_name = request.POST['your_name']
        Email_name = request.POST['email']
        Password = make_password(request.POST['Password'])
        if Person.objects.filter(Email_name=Email_name).exists():
            messages.error(request, "email number already exists")
            return redirect('/')

        else:
            Person.objects.create(first_name=first_name,
                                  Email_name=Email_name, Password=Password)
            return redirect('/login/')


# creat login page


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

