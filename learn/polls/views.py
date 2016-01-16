from django.http import Http404
from django.shortcuts import get_object_or_404, render
# Create your views here.

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = 'polls/index.html'
    context = {
    	'latest_question_list': latest_question_list,
    }
    return render( request, template, context )

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    template = 'polls/detail.html'
    context = {
        'question': question,
        'response': 'You\'re looking at question ',
    }
    return render( request, template, context )

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    template = 'polls/partial.html'
    context = {
        'question': question,
        'response': 'You\'re looking at the results of question ',
    }
    return render( request, template, context )

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    template = 'polls/partial.html'
    context = {
        'question': question,
        'response': 'You\'re voting on question ',
    }
    return render( request, template, context )