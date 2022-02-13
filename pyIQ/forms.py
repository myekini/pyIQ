from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class QuestionForm(forms.ModelForm):
     class Meta:
         model = Question
         fields = "__all__"
    
