from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.core.urlresolvers import reverse as URL_reverse
from .models import Question

'''
def index(request):
	lastest_question_list = Question.objects.order_by('-pub_date')[:5]
	#output = ', '.join([q.question_text for q in lastest_question_list])
	template = loader.get_template('polls/index.html')
	context = {
		'lastest_question_list': lastest_question_list,
	}
	return HttpResponse(template.render(context, request))
'''

def index(request):
	lastest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'lastest_question_list': lastest_question_list}
	return render(request, 'polls/index.html', context)
	
'''
def detail(request, question_id):
	#return HttpResponse( 'Youre looking at question %s.' % question_id)
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})
'''

def detail(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/detail.html', {'question': question})
	
'''
def results(request, question_id):
	response = 'Youre looking at the results of question %s'
	return HttpResponse( response % question_id)
'''

def results(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/results.html', {'question': question})
	
'''
def vote(request, question_id):
	return HttpResponse( 'Youre voting on question %s.' % question_id)
'''

def vote(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#redisplay the question voting form.
		return render(request, 'polls/detail.html', {'question': question, 'error_message': "you didn't select a choice."})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		#always return an HttpResponseRedirect after succesfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button
		return HttpResponseRedirect(URL_reverse('polls:results', args=(question.id,)))