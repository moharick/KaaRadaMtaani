from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('signout')
    else:
        if request.user.id == 1:
            if request.method == 'POST':
                form = MtaaForm(request.POST)
                if form.is_valid():
                    mtaa = Mtaa(mtaa_name=request.POST['mtaa_name'])
                    mtaa.save()
                return redirect('index')
            else:
                form = MtaaForm()
            mtaas = Mtaa.objects.all()
            return render(request,'index.html',{'mtaas':mtaas,'form':form})
        elif request.user != 1:
            user = UserProfile.objects.filter(user = request.user).first()
            if user is None:
                user = UserProfile(user=request.user)
                user.save()
            if user.mtaa_name is None:
                title = 'mtaa'
                mtaas = Mtaa.objects.all()
                return render(request,'index.html',{'mtaas':mtaas})
            else:
                user = UserProfile.objects.filter(user = request.user).first()
                return redirect(reverse('mtaa',args=[user.mtaa_name.id]))