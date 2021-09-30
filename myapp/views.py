from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from myapp.models import MyappStudent
from django.db import models
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def myview(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def Insertrecord(request):
    if request.method=="POST":
        saverecord= MyappStudent(user_name=request.POST['name'], mail_id=request.POST['Email'],
        phone_number=request.POST['phone'],address=request.POST['address'],password=request.POST['pws'],
        confirm_password=request.POST['confirmpws'])
        saverecord.save()
        print(saverecord)
        messages.success(request,'Record saved succesfully.....!')
        return render(request,'signup.html')
    

def show(request):
    a=MyappStudent.objects.get(user_name="SIVA")
    print(a.user_name)
    return HttpResponse("success")

def log(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['phone']
            upass = fm.cleaned_data['pws']
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else:          
        fm = AuthenticationForm()
        return render(request,   {'form':fm})

def profile(request):
    return render(request, 'profile.html')






