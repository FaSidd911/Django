from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import  authenticate #add this
from django.contrib.auth import login as auth_login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime
from .models import SocietyList,MembersList
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render



def login_request(request):
    if request.method == "POST":
        print('here')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request,user)
                messages.info(request, f"You are now logged in as {username}.")
                query_results = SocietyList.objects.all()   
                return render(request, "addSociety.html",{'query_results':query_results})
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", {"login_form":form})

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')
