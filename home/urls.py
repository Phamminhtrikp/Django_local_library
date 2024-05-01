from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
   path('', views.home, name='home'),
   path('signup', views.signup, name='signup'),
   path('signin', views.signin, name='signin'),
   path('signout', views.signout, name='signout'),
   
   path('index',views.index,name="index"),
   path('add/',views.add,name="add"),
   path("addrec/",views.addrec,name="addrec"),
   path('delete/<int:id>/',views.delete,name="delete"),
   path('update/<int:id>/',views.update,name="update"),
   path('update/uprec/<int:id>/',views.uprec,name="uprec"),
]