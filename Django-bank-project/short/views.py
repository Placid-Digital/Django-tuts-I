import logging

from django.contrib.auth import user_logged_in, signals
from django.dispatch import receiver
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            messages.success(
                request, f'Your account has been created! You are now able to login')
            return redirect('users/login.html')
        else:
            return HttpResponse(form.errors)    
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def login(request):
    if request.method == 'POST':
        form =  user_logged_in(request.POST)
        if form.is_valid():
            form.save()
            username = form.is_valid('username')
            password = form.is_valid('password')
            messages.success(
                request, 'successful login')
            return redirect('short/profile/')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/profile.html', context)

#
# @receiver(user_logged_in)
# def user_logged_in(sender, users, request, **kwargs):
#     logger = logging.getLogger(__name__)
#     logger.info("users logged in: %s at %s" % (users, request.META['REMOTE_ADDR']))


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users/profile.html')
    else:

        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
