from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'commonapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'commonapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'commonapp/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # print(request.POST['choice'])
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'commonapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('commonapp:results', args=(question.id,)))

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('commonapp/index.html')
#     # context = {
#     #     'latest_question_list': latest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'commonapp/index.html', context)
#
# def detail(request, question_id):
#     # return HttpResponse("You're looking at question %s." % question_id)
#     # try:
#         # question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#         # raise Http404("Question does not exist")
#     # return render(request, 'commonapp/detail.html', {'question': question})
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'commonapp/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'commonapp/results.html', {'question': question})
#
