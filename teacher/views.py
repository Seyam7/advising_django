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
from .models import admin,addcourse
from teacher.models import msg
from django.db import connection

# Create your views here.


def admin1(request):
    noti=""
    user_list=admin.objects.all()
    if request.method=="POST":
        email=request.POST.get("email")
        adpass=request.POST.get("adpass")
        if(user_list.filter(email=email)):
            if(user_list.filter(adpass=adpass)):
                return redirect('adHome')
            else:
                noti=1
                return render(request,'teacher_login.html',{'noti':noti})
        else:
            noti=2
            return render(request,'teacher_login.html',{'noti':noti})
    return render(request,'teacher_login.html')

def allcourse(request):

    course_list=addcourse.objects.all()

    return render(request,'allcourse.html',{"course_list":course_list})


def adHome(request):
    

    return render(request,'teacher_home.html')

def add_course(request):
    messages=msg.objects.all()
    noti=""
    user_list=addcourse.objects.all()
    if request.method=="POST":
        courseName=request.POST.get("courseName")
        courseCode=request.POST.get("courseCode")
        credit=request.POST.get("credit")

        if( user_list.filter( courseName=courseName)):

            noti=1
            return render(request,'add_course.html',{'noti':noti})

        elif( user_list.filter( courseCode=courseCode)):
            noti=2
            return render(request,'add_course.html',{'noti':noti})
        else:
            messages.delete()
            noti=3
            add_c=addcourse(courseName=courseName, courseCode=courseCode, credit=credit)
            add_c.save()
            return render(request,'add_course.html',{'noti':noti,'messages':messages})

    return render(request,'add_course.html')





def logoutuser(request):
    noti=""
    
    return redirect("login")


def delet(request,x):
    course_list=addcourse.objects.all()
    #student=course_list.filter(courseCode =x)
    #student.delete()

    with connection.cursor() as cursor:
        cursor.callproc('delete_sub', [x])
    return render(request,'allcourse.html',{"course_list":course_list})

