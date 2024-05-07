from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import redirect
from django.contrib import messages
from .models import student
# Create your views here.

def login(request):
    noti=""
    user_list=student.objects.all()
    if request.method=="POST":
        p_email=request.POST.get("p_email")
        password=request.POST.get("password")
        if(user_list.filter(p_email=p_email)):
            if(user_list.filter(password=password)):
                request.session['name'] = p_email
                return redirect('studentHome')
            else:
                noti=1
                return render(request,'login.html',{'noti':noti})
        else:
            noti=2
            return render(request,'login.html',{'noti':noti})
    return render(request,'login.html')


def signup(request):
    user_list=student.objects.all()
    if request.method=="POST":
        first_name=request.POST["first_name"]
        lastName=request.POST["lastName"]
        gender=request.POST["gender"]
        p_email=request.POST["p_email"]
        phone=request.POST["phone"]
        password=request.POST.get("password")
        con_Pass=request.POST['con_Pass']
      
        if(user_list.filter(p_email=p_email)):
            noti=2
        else:
            if(password==con_Pass):
                add_student=student(first_name=first_name,lastName=lastName,gender=gender,p_email=p_email,phone=phone,password=password)
                add_student.save()
                request.session['name'] = p_email
                return redirect('studentHome')
            noti=1
        return render(request,'signup.html',{'noti':noti})
    return render(request,'signup.html')