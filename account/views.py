from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from . import models
from . import forms
import os

# Create your views here.
def signup_view(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            #form.save()
            #note='کاربر با نام %s ایجاد شد.' % (form.cleaned_data['username'])
            login(request,user)
            return redirect('index')
    else:
        form=UserCreationForm()
    return render(request,'account/SignUp.html',{'form':form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            #form.save()
            #note='کاربر با نام %s ایجاد شد.' % (form.cleaned_data['username'])
            login(request,user)
            return redirect('index')
    else:
        form=AuthenticationForm()
    return render(request,'account/Login.html',{'form':form})

def logout_view(request):
    if request.method=="POST":
        logout(request)
    return render(request,'account/Logout.html')