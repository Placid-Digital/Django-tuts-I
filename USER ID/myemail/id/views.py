import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView,View
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import redirect
from django.contrib import messages
# signal hera 

from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


from id.models import Person

# from django.http import HttpResponse

# create SIGNAL hera

 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
 
 
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
 
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
 
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
 
    return render(request, 'users/profile.html', context)




# Create your views here.

def view(request):
    render('home.html')

def login_page(request):
   return render(request, 'id/login.html')

def welcome_page(request):
       return render(request, 'id/welcome.html')

# create Table data form
def data(request):
       persons = Person.objects.filter(is_active=True).order_by('id')
       
       return render(request, 'id/table.html', context={
           'request': request,
           'persons': persons,
       })


def index(request):
    return render(request,'id/home.html', context={})

def home(request):
    return render(request,'id/login.html', context={})

def successful(request):
    return render(request,'id/welcome.html', context={})



def home(request):
    return("this is my first page.")

def login(request):
    return("this is my first page.")

def welcome(request):
    return("this is my first page.")

def dataon(request):
    return("this is my first page.")


class AboutUs(View):
      def get(self, request, *args, **kwargs):
        return render(request, "home.html")

class loginus(View):
      def get(self, request, *args, **kwargs):
        return render(request, "login.html")

class welcomeus(View):
      def get(self, request, *args, **kwargs):
        return render(request, "welcome.html")

class dataus(View):
      def get(self, request, *args, **kwargs):
        return render(request, "table.html")

     
    
#  create home form   
def form_data(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        Company_name=request.POST['company']
        Email_name=request.POST['Email']
        Phone_number=request.POST['Phone']
        Password=make_password(request.POST['Password'])
        if Person.objects.filter(Phone_number=Phone_number).exists():
            messages.error(request,"phone number already exists")
            return redirect('/')
            
        elif Person.objects.filter(Email_name=Email_name).exists():
            messages.error(request,"Email id already exists")
            return redirect('/')
    
        else:    
            Person.objects.create(first_name=first_name,
                            last_name=last_name,Company_name=Company_name,
                            Email_name=Email_name,Phone_number=Phone_number,Password=Password)
            return redirect('/login/')
# creat delete button 
def delete_user(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        uid = json.loads(data)
        print(uid)
        if Person.objects.filter(id=uid).exists():
            Person.objects.filter(id=uid).update(is_active=False)
            return JsonResponse({"staus": True, "message": "User has been deleted"})
        else:
            return JsonResponse({"staus": False, "message": "User not exists."})
    else:
        return JsonResponse({"staus": False, "message": "Method not allowed."})

# create login form 
def Login_form(request):
        if request.method == 'POST':
            Phone_number=request.POST['Phone']
            User_Password=request.POST['Password']
            if Person.objects.filter(Phone_number=Phone_number).exists():
                obj = Person.objects.get(Phone_number=Phone_number)
                Password=obj.Password
                if check_password(User_Password,Password):
                    return redirect('/welcome/')
                else:
                    return HttpResponse('password incorrect')
            else:
                return HttpResponse('phone number is not registered')

# creat Edit button
def update_view(request,uid):
    res = Person.objects.get(id=uid)
    return render(request,'id/update.html', context={
        
        'person': res,
    })


     
def update_form_data(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        Company_name=request.POST['company']
        Email_name=request.POST['Email']
        Phone_number=request.POST['Phone']
        
          
        Person.objects.filter(id=uid).update(first_name=first_name,
                            last_name=last_name,Company_name=Company_name,
                            Email_name=Email_name,Phone_number=Phone_number)
        return redirect('/data/')
        # redirect to table form
        
        
                    
       
                    

        

        
        