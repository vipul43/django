from django.shortcuts import render, get_object_or_404

# Create your views here.

#NOTE: Every function in views has a request parameter which is mandatory
#       Also every function in views returns HttpResponse which is mandatory too

from django.http import HttpResponse, Http404, HttpResponseRedirect

import datetime

def getTime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


#adding more views
from polls.models import Question

from django.template import loader

from django.views import generic

from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

from django.urls import reverse

#NOTE: Always return an HttpResponseRedirect after successfully dealing
#       with POST data. This prevents data from being posted twice if a
#       user hits the Back button.

#this vote function is now connected with the front end detail page
#after selecting an option in the detail page form
#the request is sent to this backend vote function using POST method
#then depending on the choice selected in the detail page this function responds
#and loads either the results page or detail page again
def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError or Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
