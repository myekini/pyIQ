from django.shortcuts import redirect, render
from django.urls import reverse
from pyIQ.models import Question
from pyIQ.forms import QuestionForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    """view first page"""
    if request.method =='POST':
        print(request.POST)
        questions = Question.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total +=1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
            }
        return render(request,'pyIQ/result.html',context)

    else:
        questions = Question.objects.all()
        context = {'questions': questions}
        return render(request, 'pyIQ/index.html', context)


@login_required
def add_question(request):
    """ add quiz questions and options """
    if request.user.is_staff:
        questions = Question.objects.all()
        if request.method != 'POST':
            form = QuestionForm()
        else:
            form = QuestionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('pyIQ:index')
        context = {'questions': questions, 'form': form}
        return render(request, 'pyIQ/add_question.html', context)
    else:
        return redirect('pyIQ:index')