from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'pyIQ'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_question/', views.add_question, name='add_question'),
]