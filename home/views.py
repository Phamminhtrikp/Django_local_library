from django.shortcuts import render, redirect
from .models import myblog, Users  # Assuming your model is named MyBlog
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone, dateformat

def home(request):
    blogs = myblog.objects.all()  # Renaming the variable to avoid conflicts
    return render(request, 'home.html', {'blogs': blogs})  # Adjusted context variable name


def signup(request):
    return render(request, 'authentication/signup.html')



def signin(request):
    #print( 'requets:' , request)
    if request.method == 'POST':
        
        #print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( username = username, password = password)
        print(user)
        if user is not None:
            
            login(request, user)
            users=Users.objects.all()
            return render(request, 'crud/index.html', {'users':users})
        else:
            messages.error(request, 'Bad credentials')
            redirect('home')


    return render(request, 'authentication/signin.html')


def signout(request):
    logout(request)
    return redirect('home')


#CRUD

def index(request):
    user=Users.objects.all()
    return render(request,'crud/index.html',{'user':user})

def add(request):
    return render(request,'crud/add.html')

def addrec(request):
    x=request.POST['username']
    y=request.POST['email']
    z=request.POST['password']
    k=request.POST['status']
    h= dateformat.format(timezone.localtime(timezone.now()), 'Y-m-d H:i:s') 
    user=Users(username=x,email=y,password=z, status=k, created_at=h)
    user.save()
    return redirect("/index")

def delete(request,id):
    user=Users.objects.get(id=id)
    user.delete()
    return redirect("/index")

def update(request,id):
    user=Users.objects.get(id=id)
    return render(request,'crud/update.html',{'user':user})

def uprec(request,id):
    x=request.POST['username']
    y=request.POST['email']
    z=request.POST['password']
    k=request.POST['status']
    user=Users.objects.get(id=id)
    user.username=x
    user.email=y
    user.password=z
    user.status=k
    user.save()
    return redirect("/index")