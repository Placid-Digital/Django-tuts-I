import json
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
from .models import Person


# create Table data form
def data(request):
    persons = Person.objects.filter(is_active=True).order_by('id')

    return render(request, 'shadi/table.html', context={
        'request': request,
        'persons': persons,
    })


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


# creat Edit button
def update_view(request, uid):
    res = Person.objects.get(id=uid)
    return render(request, 'shadi/update.html', context={

        'person': res,
    })


def update_form_data(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        first_name = request.POST['first_name']
        contact = request.POST['contact']
        Email_name = request.POST['Email']
        Phone_number = request.POST['Phone']

        Person.objects.filter(id=uid).update(first_name=first_name,
                                             contact=contact,
                                             Email_name=Email_name, Phone_number=Phone_number)
        return redirect('/data/')

# users registraction form

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="shadi/register.html", context={"register_form": form})
