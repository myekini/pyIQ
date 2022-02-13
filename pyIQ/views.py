from django.shortcuts import render
from django.urls import reverse
from pyIQ.models import Question
from pyIQ.forms import QuestionForm
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    """view first page"""
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'pyIQ/index.html', context)
