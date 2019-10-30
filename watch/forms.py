from django import forms
from django.forms import ModelForm
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class MtaaForm(ModelForm):
    class Meta:
        model = Mtaa
        fields = ('mtaa_name',)

class AddBizForm(ModelForm):
    class Meta:
        model = Biz
        fields = ('name','biz_location','email')

class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','mtaa_name',)

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','post_description',)