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

def base(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')

def index(request):
    return render(request,'index.html')

# def login(request):
#     return render(request,'login.html')

def contact(request):
    return 0

@login_required
def addSociety(request):
    if request.method == "POST":
        societyName = request.POST.get('societyName')
        societyNameExists = SocietyList.objects.filter(societyName=societyName)
        if societyNameExists:
            return HttpResponseRedirect('addSociety')
        regno = request.POST.get('regno')
        address = request.POST.get('address')
        new_society = SocietyList(societyName=societyName, regno=regno, address=address, date_add_society=datetime.today())
        new_society.save()   
        messages.success(request, 'Your message has been sent!')        
    query_results = SocietyList.objects.all()        
    return render(request, 'addSociety.html',{'query_results':query_results})


@login_required
def societyMembers(request, item_name):
    if request.method == "POST":
        societyName = item_name
        memberName = request.POST.get('memberName')
        memberNameExists = MembersList.objects.filter(memberName=memberName)
        if memberNameExists:
            return HttpResponseRedirect('societyMembers')
        flatno = request.POST.get('flatno')
        openingBalance = request.POST.get('openingBalance')
        closingBalance = request.POST.get('closingBalance')
        new_member = MembersList(societyName=societyName, memberName=memberName, flatno=flatno, openingBalance=openingBalance,closingBalance=closingBalance, date_add_member=datetime.today())
        new_member.save() 
    item = get_object_or_404(SocietyList, societyName=item_name)
    query_results = MembersList.objects.all()  
    context = {
        'item': item,
        'query_results': query_results,
     }
    return render(request, 'societyMembers.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')