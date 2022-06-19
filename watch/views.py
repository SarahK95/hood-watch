from distutils import log
from multiprocessing.dummy import current_process
import profile
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
import datetime as dt
from django.contrib.auth.models import User
from .forms import ProfileForm,PostForm,BusinessForm,CommentForm


# Create your views here.
def home(request):
    try:
        if not request.user.is_autheniicated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile = Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-prof')
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    profile = Profile.objects.get(username = current_user)
    posts = Post.objects.filter(neighbourhood =profile.neighbourhood)
    return render(request, 'post.html', {'posts':posts})
    
@login_required(login_url='/accounts/login')
def police(request):
    current_user = request.user
    profile = Profile.objects.get(username= current_user)
    polices = Police.objects.filter(neighbourhood =profile.neighbourhood) 
    return render (request, 'police.html', {'polices':polices}) 

@login_required(login_url='/accounts/login')
def health(request):
    current_user = request.user
    profile = Profile.objects.get(username = current_user)
    healthdepts =Health.objects.filter(neighbourhood=profile.neighbourhood)  
    return render(request, 'health,html', {'healthdepts': healthdepts})
    
@login_required(login_url='/accounts/login/')
def businesses(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)
    return render(request,'business.html',{"businesses":businesses})  

@login_required(login_url='/accounts/login/')
def view_post(request,id):
    current_user = request.user
    try:
        comments = Comment.objects.filter(post_id=id)
    except:
        comments =[]

    post = Post.objects.get(id=id)
    if request.method =='POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username = current_user
            comment.post = post
            comment.save()
    else:
        form = CommentForm()
    return render(request,'view_post.html',{"post":post,"form":form,"comments":comments})
    
    

    




