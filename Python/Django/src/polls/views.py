from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.

def index(request):
    return HttpResponse("Hello world.\nYou're at the polls index.")


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    # gets shortened to:
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # above was used before template was set up
    # template = loader.get_template('polls/index.html') no longer needed due to render function
    context = {'latest_question_list': latest_question_list,}
    # return HttpResponse(template.render(context, request)) gets shortcutted by below
    return render(request, 'polls/index.html', context)
    # The render() function takes the request object as its first argument, 
    # a template name as its second argument 
    # and a dictionary as its optional third argument