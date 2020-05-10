from django.shortcuts import render

# Create your views here.

#NOTE: Every function in views has a request parameter which is mandatory
#       Also every function in views returns HttpResponse which is mandatory too

from django.http import HttpResponse, Http404
import datetime

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def getTime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


#adding more views
from polls.models import Question

def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')

    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse("You're looking at results of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on the question %s." % question_id)


#adding more functional views


from django.template import loader

def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_questions_list': latest_questions_list
    }
    return HttpResponse(template.render(context, request))
