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
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile = Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-prof')
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'blog' in request.GET and request.GET["blog"]:
        search_term = request.GET.get("blog")
        searched_posts = Post.search_blogpost(search_term)
        message=f"{search_term}"
        print(searched_posts)
        return render(request,'search.html',{"message":message,"blogs":searched_posts})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})

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
def my_prof(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)
    return render(request,'profile.html',{"profile":profile})

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

@login_required(login_url='/accounts/login/')
def user_profile(request,username):
    user = User.objects.get(username=username)
    profile =Profile.objects.get(username=user)
    return render(request,'profile.html',{"profile":profile})

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user=request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')
    else:

        form = ProfileForm()
    return render(request,'profile_form.html',{"form":form})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(username=current_user)
        form =ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return redirect('home')
    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()
    return render(request,'profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_biz(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    if request.method=="POST":
        form =BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit = False)
            business.owner = current_user
            business.hoody = profile.neighbourhood
            business.save()
        return HttpResponseRedirect('/businesses')
    else:
        form = BusinessForm()
    return render(request,'biz_form.html',{"form":form})
    
    
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)
    if request.method=="POST":
        form =PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.username = current_user
            post.hood = profile.neighbourhood
            post.image = profile.image
            post.save()
        return HttpResponseRedirect('/post')
    else:
        form = PostForm()
    return render(request,'post_form.html',{"form":form})    

    




