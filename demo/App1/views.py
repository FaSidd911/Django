from django.shortcuts import render, HttpResponse

# Create your views here.

def base(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def contact(request):
    return HttpResponse ('I am liar')