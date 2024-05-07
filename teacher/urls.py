from operator import concat
from django.urls import path
from .import views



urlpatterns=[
    path('', views.admin1,name="admin"),
    path('adHome/', views.adHome,name="adHome"),
    path('add_course/', views.add_course,name="add_course"),
    path('allcourse/', views.allcourse,name="allcourse"),
    path('delet/<x>/', views.delet,name="delet"),
]

