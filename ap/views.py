from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .models import *
# Create your views here.


def Maktab(request):
    return render(request,'home.html')
def Maktab6(request):
    return render(request,'playlist.html')
def Maktab9(request):
    return render(request,'teacher_profile.html')
def Maktab10(request):
    return render(request,'teachers.html')
def Maktab11(request):
    return render(request,'update.html')
def Maktab12(request):
    return render(request,'watch-video.html')

def Aloqaga(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        msg = request.POST.get("msg")
        Aloqa.objects.create(name=name,email=email,number=number,msg=msg)
        print(name,email,number,msg)
    return render(request,'contact.html')

def playlist(request,name):
    obj = Faxrimiz.objects.get(name=name)
    Author1 = Author.objects.all()
    return render(request,'playlist.html',{"obj":obj,"Author":Author1})

def bizning(request):
    context = Faxrimiz.objects.all()
    return render(request,'courses.html',{"context":context})

def teacher_profile(request,name):
    con = Uqituv.objects.get(name=name)
    Author2 = Authorr.objects.all()
    return render(request,'teacher_profile.html',{"con":con,"Authorr":Author2})

def teacher(request):
    context2 = Uqituv.objects.all()
    return render(request, 'teachers.html',{"context2":context2})

def about(request):
    context3 = About.objects.all()
    return render(request, 'about.html',{'context3':context3})

def direktor(request):
    context4 = Direktor.objects.all()
    return render(request, 'profile.html',{'context4':context4})

def Register(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 !=password2:
            context['error']= "Second password is wrong please checked"
            return render(request,'register.html',context)
        if first_name=="" or last_name=="" or user_name=="" or password1=="" or password2=="":
            context['error']="Check your information, pleace"
            return render(request,'register.html',context)
        user_check = User.objects.filter(username=user_name)
        if len(user_check)!=0:
            context['error']="This User already taken please other username"
            return render(request,'register.html',context)

        print('user created')
        user = User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password1)
        user.save()
        print(user_name,first_name)

    return render(request,'register.html')

def Signin(request):
    return render(request,'login.html')


