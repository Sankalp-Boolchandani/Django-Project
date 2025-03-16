from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.

def index(request):
  return render(request, 'index.html', {"page":"Index"})

def register_user(request):
  if request.method=='POST':
    data=request.POST
    first_name=data.get('first_name')
    last_name=data.get('last_name')
    contact=data.get('contact')
    email=data.get('email')
    password=data.get('password')
    password=make_password(password, None, hasher='default')

    user=Employee.objects.filter(email=email)
    if user.exists():
      messages.error(request, "Email already exists.")
      return redirect("/register_user")
    else:
      user=Employee.objects.create(
      first_name=first_name,
      last_name=last_name,
      contact=contact,
      email=email,
      password=password,
    )
    if user:
      messages.success(request, "User created!")
      return redirect("/register_user")

  context={"page":"Register"}
  return render(request, 'register_user.html', context)