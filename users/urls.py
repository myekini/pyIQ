from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), {'template_name':'registration/login.html'} , name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register')
]