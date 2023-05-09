from django.shortcuts import *
from .models import *
from django.http import JsonResponse
from math import *
from datetime import*

# Create your views here.
def home(request):
    
    post=Post.objects.all()
    params={"post":post}
    return render(request,"home.html",params)
def test(request):
    return render(request,"test.html")
def login(request):
    if request.method == 'POST':
        name=request.POST.get("name1","")
        Passward=request.POST.get("passs","")
        cname=Profiles.objects.filter(name=name).values('name')
        c1name=cname
        cpassword=Profiles.objects.filter(name=name).values('Passward')
        # print(cname,cpassword)
        # print(name,Passward)
        
        
        dat=Cuser(name=cname)
        dat.save()
        # userdet=Profiles(name=name,email=email,mobile=mobile,age=age,gender=gender,Passward=Passward)
        # userdet.save()
    res=redirect('/')
    return render(request,"login.html")

def signin(request):
    if request.method == 'POST':
        name=request.POST.get("name1","")
        email=request.POST.get("email1","")
        mobile=request.POST.get("Mobile","")
        age=request.POST.get("age","")
        gender=request.POST.get("gender","")
        Passward=request.POST.get("passs","")
        print(name,email)
        userdet=Profiles(name=name,email=email,mobile=mobile,age=age,gender=gender,Passward=Passward)
        userdet.save()
    return render(request,"signin.html")
def profile(request):
    user=Cuser.objects.all()
    post=Post.objects.filter(name="ajith")
    
    # print(user[0].Username)    
    
    return render(request,"profile.html",{"user":user,"post":post})

def search(request):
    return render(request,"search.html")