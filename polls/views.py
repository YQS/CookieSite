from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
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
	
def detail(request, question_id):
	return HttpResponse( 'Youre looking at question %s.' % question_id)

def results(request, question_id):
	response = 'Youre looking at the results of question %s'
	return HttpResponse( response % question_id)
	
def vote(request, question_id):
	return HttpResponse( 'Youre voting on question %s.' % question_id)