from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth.models import User
import datetime

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

def signout(request):
    logout(request)
    return redirect('/accounts/login')

def mtaa(request,mtaa_id):
    if request.user.id == 1:
        mtaa = Mtaa.objects.get(id = mtaa_id)
        members = UserProfile.objects.filter(mtaa = mtaa).all()
        return render(request,'mtaa.html',{'mtaa':mtaa,'members':members})
    else:
        mtaa = Mtaa.objects.get(id = mtaa_id)
        user = UserProfile.objects.filter(user = request.user).first()
        bizs = Biz.objects.filter(biz_mtaa=mtaa).all()
        user.mtaa = mtaa
        user.save()

        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = Post(title=request.POST['title'],post_description=request.POST['post_description'],posted_by=request.user,post_hood=mtaa,posted_on=datetime.datetime.now())
                post.save()
                return redirect(reverse('mtaa',args=[mtaa.id]))
        else:
            form = PostForm()

        posts = Post.objects.filter(post_hood = mtaa).all()
        return render(request,'mtaa.html',{'posts':posts,'form':form,'user':user,'bizs':bizs,'mtaa':mtaa,})


def profile(request,user_id):
    user = User.objects.get(id = user_id)
    profile = UserProfile.objects.filter(user = user).first()
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,instance=profile)
        if form.is_valid():
            profile.first_name = request.POST['first_name']
            profile.last_name = request.POST['last_name']
            profile.save()
        return redirect(reverse('profile',args=[user.id]))
    else:
        form = UpdateProfileForm(instance=profile)

    bizs = Biz.objects.filter(owner = user).all()
    mtaas = Mtaa.objects.all()

    return render(request,'profile.html',{'mtaas':mtaas,'bizs':bizs,'profile':profile,'form':form})


def add_biz(request):
    user = User.objects.filter(id = request.user.id).first()
    profile = UserProfile.objects.filter(user = user).first()
    if request.method == 'POST':
        biz_form = AddBizForm(request.POST)
        if biz_form.is_valid():
            biz = Biz(name = request.POST['name'],owner = user,biz_mtaa = profile.mtaa,email=request.POST['email'])
            biz.save()
        return redirect(reverse('profile',args=[user.id]))
    else:
        biz_form = AddBizForm()
    return render(request,'biz.html',{'biz_form':biz_form})



def search(request):
    try:
        if 'biz' in request.GET and request.GET['biz']:
            search_term = request.GET.get('biz')
            searched_biz = Biz.objects.get(name__icontains=search_term)
            return render(request,'search.html',{'searched_biz':searched_biz})
    except (ValueError,Biz.DoesNotExist):
        message = "Oops! We couldn't find the biz you're looking for."
        return render(request,'search.html',{'message':message})
    return render(request,'search.html',{'message':message,'searched_business':searched_biz})
