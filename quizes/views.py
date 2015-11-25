from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from .models import Question, Choice, Category
# Create your views here.
def index(request):
    latest_category_list = Category.objects.order_by('id')
    context = {'latest_category_list': latest_category_list}
    return render(request, 'quizes/index.html', context)


#i am saving previous version of quiz here down in comments
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'quizes/index.html', context)

def detail(request, category_id):
    category1 = get_object_or_404(Category, pk=category_id)
    question_list = Question.objects.filter(category = category1.id)
    context = {'question_list' : question_list}
    return render(request, 'quizes/detail.html', context)

# category.category_name = Question.category
#i am saving previous version of quiz here down in comments
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'quizes/detail.html', {'question': question})

def results(request, quiz_id):
    # question = get_object_or_404(Question, pk=question_id)
    list1 = ['physics', 'chemistry', 1997, 2000];
    context = {'message': list1}
    # return render(request, 'quizes/results.html', {'question': question})
    return render(request, 'quizes/results.html', context)

# def submit(request, question_id):
#     p = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'quizes/detail.html', {
#             'question': p,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         # selected_choice.votes += 1#this is omited by me probably i will include after i include users
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('quizes:results', args=(p.id,)))