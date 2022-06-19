from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
import datetime as dt
from django.contrib.auth.models import User


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
    
    
    
    
    
    
    
    
    
    
    
    
    #     try:
    #     if not request.user.is_authenticated:
    #         return redirect('/accounts/login/')
    #     current_user=request.user
    #     profile =Profile.objects.get(username=current_user)
    # except ObjectDoesNotExist:
    #     return redirect('create-profile')

    # return render(request,'index.html')