from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView

from .forms import *

# Create your views here.

def logout_view(request):
    """ log you out """
    logout(request)
    return HttpResponseRedirect(reverse('pyIQ:index'))

def register(request):
    """ register users """
    if request.method != 'POST':
        form = RegistrationForm()
        
    else:
        form = RegistrationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # log the user in and then redirect to the home
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('pyIQ:index'))
    context = {'form':form}
    return render(request, 'registration/register.html', context)
            
