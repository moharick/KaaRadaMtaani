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