from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,logout,login
from django.shortcuts import render,redirect
from .models import Blog,Personal
from django.db import connection, transaction
from django.views.generic.base import View
from datetime import datetime

# Create your views here.

#this is base template having bootstrap navbar...
def base(request):
    return render(request,'base.html')

#index page / Home page
def index(request):
    data=Blog.objects.all()
    data=reversed(data) 
    context={'all_blog':data} 
    return render(request,'index.html',context)

#authenticated user profile page...
def profile(request):
    #check if user is anonymous,redirect to index page/home page
    if request.user.is_anonymous:
        return redirect('/') 
    #if user is authenticated
    data=Blog.objects.filter(user_id=request.user.id)
    data=reversed(data)
    pic_bio=Personal.objects.filter(uname=request.user.username)
    context={'all_blog':data,'pic_bio':pic_bio} 
    return render(request,'profile.html',context)

#to add new blog...
def add_blog(request):
    #to submit a new blog..
    if request.method=='POST':     
        title=request.POST.get('title')
        text=request.POST.get('desc')
        blog=Blog.objects.create(title=title,text=text,user_id=request.user.id,uname=request.user.username,date=datetime.now())
        blog.save()
        return redirect('/')
    else:
        return render(request,'add_blog.html')

#To see another user profile
def anotheruser(request,blog_uname=None):
    data=Blog.objects.filter(uname=blog_uname)
    userx=User.objects.get(username=blog_uname)
    try:
        userp=Personal.objects.get(uname=blog_uname)
    except:
        userp=None
    context={'all_blog':data,'userx':userx,'userp':userp}
    return render(request,'anotheruser.html',context)

#to delete current user post...
def delete_post(request,post_id=None):
    ids=Blog.objects.filter(pk=post_id)   
    ids.delete()
    return redirect('profile')

#to delete profile picture and bio of authenticated user...
def delete_bio(request,pic_bio=None):
    ids=Personal.objects.filter(bio=pic_bio)
    ids.delete()
    return redirect('edit')

#to save new profile picture and bio of authenticated user...       
def edit(request):
    #if user pic and bio doesn't exists...
    if request.method=='POST':
        picture=request.FILES['user_pic']
        bios=request.POST['user_bio']
        userp=request.user.username
        user_pic_bio=Personal.objects.create(uname=userp,bio=bios,pic=picture)
        user_pic_bio.save()
        return redirect('profile')     
    #if user pic and bio exist 
    u_edit=Personal.objects.filter(uname=request.user.username)
    context={'pic_bio':u_edit}
    return render(request,'edit.html',context)


#login is for login existing user...
def LoginUser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        #check user is valid or not
        if user is not None:              
            login(request,user)
            return redirect('profile')
        else:
            return render(request,'login.html') 
    else:
        return render(request,'login.html')

#signup to create new account....
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']

        #check if username and email are exist,then redirect to signup page again else create a new account...
        if User.objects.filter(username=username).exists():
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            return redirect('signup')
        else:
            x=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            x.save()
            return redirect('profile')
    return render(request,'signup.html')


#logout user and redirect to index/home page
def LogoutUser(request):
    logout(request)
    return redirect('/')

#this is about page 
def about(request):
    return render(request,'about.html')
