from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.


#homepage view.
#to learn how to create views with render.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:4]
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request, '/polls/index.html', context)

def detail(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id) 
    except Question.DoesNotExist:
        raise Http404 ("Question does not exist.")

    return render (request, 'polls/detail.html', {'question': question})

def results (request, question_id):
    return HttpResponse("You are looking at the results of question number  %s."% question_id)

def vote(request, question_id):
    response = "You are voting for question number: %s"
    return HttpResponse(response % question_id)
