import email
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from user.models import user


def view(request):
    render('home.html')

# def login_page(request):
#    return render(request, 'users/login.html')
#
# def regiseter(request):
#        return render(request, 'users/regiseter.html')


def home(request):
    return render(request, 'users/home.html')

#
#
# def home(request):
#     return render(request,'users/home.html', context={})
#
# def login(request):
#     return render(request,'users/login.html', context={})





#
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             messages.success(request, f'Your account has been created. You can log in now!')
#             return redirect('users/login.html')
#     else:
#         form = UserCreationForm()
#
#     context = {'form': form}
#     return render(request, 'users/register.html', context)


def regiseter(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        contact = request.POST['contact']
        Email_name = request.POST['Email']
        Phone_number = request.POST['Phone']
        Password = make_password(request.POST['Password'])
        if user.objects.filter(Phone_number=Phone_number).exists():
            messages.error(request, "phone number already exists")
            return redirect('/')

        elif user.objects.filter(email=email).exists():
            messages.error(request, "Email id already exists")
            return redirect('/')

        else:
            user.objects.create(name=first_name,
                                  contact=contact,
                                  email=email, Phone_number=Phone_number, Password=Password)
            return redirect('/login/')

def Login_form(request):
        if request.method == 'POST':
            Phone_number = request.POST['Phone']
            User_Password = request.POST['Password']
            if user.objects.filter(Phone_number=Phone_number).exists():
                obj = user.objects.get(Phone_number=Phone_number)
                Password = obj.Password
                if check_password(User_Password, Password):
                    return redirect('/home/')
                else:
                    return HttpResponse('password incorrect')
            else:
                return HttpResponse('phone number is not registered')



