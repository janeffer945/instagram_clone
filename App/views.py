from django.contrib.auth.models import User
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile,Post, Reels,Story
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("Login")
        posts = Post.objects.filter(Q(profile__followers=request.user) & ~Q(likes=request.user))
    story = Story.objects.filter(profile__followers=request.user)

    context = {"posts":posts,'stories':story}
    return render(request,'index.html',context)



# LOGIN VIEW FOR USER
def Login(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect("profile")
    return render(request,'Login.html')