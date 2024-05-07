from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import redirect
from django.contrib import messages
from teacher.models import addcourse
from .models import addsub
from django.db import connection

# Create your views here.


def studentHome(request):
    
    return render(request,'home.html')

def add(request):
    course_list=addcourse.objects.all()

    return render(request,'addcourse.html',{"course_list":course_list})

def addc(request,x):
    noti=""
    course_list=addcourse.objects.all()
    courseCode=x
    course_list2=addsub.objects.all()
    email=request.session['name']
    cc=course_list2.filter(courseCode=x)
    if(cc.filter(email=email)):
        noti=1
        return render(request,'addcourse.html',{"course_list":course_list,'noti':noti})
    else:
        noti=2
        enrollc= addsub(courseCode=courseCode,email=email)
        enrollc.save()
        return render(request,'addcourse.html',{"course_list":course_list,'noti':noti})



def enroll(request):
    list=addcourse.objects.all()
    email=request.session['name']
    course_list=addsub.objects.all()
    c_l=course_list.filter(email=email)
    return render(request,'enroll.html',{"c_l":c_l,"list":list})


def allcourses(request):

    course_list=addcourse.objects.all()

    return render(request,'allco.html',{"course_list":course_list})



def deletsub(request,x):
    list=addcourse.objects.all()
    email=request.session['name']
    course_list=addsub.objects.all()
    c_l=course_list.filter(email=email)
    #student=course_list.filter(courseCode =x)
    #student.delete()
    with connection.cursor() as cursor:
        cursor.callproc('delete_course', [x])
    return render(request,'enroll.html',{"c_l":c_l,"list":list})



def logoutuser(request):
    logout(request)
   
    return redirect("login")

