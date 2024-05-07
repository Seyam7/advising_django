from operator import concat
from django.urls import path
from .import views



urlpatterns=[
    path('', views.studentHome,name="studentHome"),
    path('logoutuser/', views.logoutuser,name="logoutuser"),
    path('add/', views.add,name="add"),
    path('enroll/', views.enroll,name="enroll"),
    path('addc/<x>/', views.addc,name="addc"),
    path('allcourses/', views.allcourses,name="allcourses"),
    path('deletsub/<x>/', views.deletsub,name="deletsub"),

]

