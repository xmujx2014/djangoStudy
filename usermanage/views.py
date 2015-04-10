from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import Person
from django.core.urlresolvers import reverse
from juaOL.utils import json_response
# Create your views here.

def teaminfo(request):
	personList = Person.objects.all()
	return render(request, 'user_manage.html', {'personList': personList})

def addPerson(request):
	attrs = ['team', 'family_name', 'given_name', 'simple_name',
		'identity_num', 'gender', 'groupe', 'category']
	personInfo = Person()
	# personInfo.id = 1
	# personInfo.team = 'e'
	# setattr(personInfo, 'team', 'h')
	person_str = '{'
	data = request.POST.get('data', '')
	print 'dd'
	print data
	for attr in attrs:
		setattr(personInfo, attr, request.POST.get(attr, ''))
	# 	personInfo.attr = request.POST.get(attr, 'NULL')
		person_str += '%s : %s; \n' % (attr, getattr(personInfo, attr))
	# personInfo.save()
	# print personInfo.team
	print person_str
	ajaxData = {
	'code': 200,
	}
	# return HttpResponseRedirect(reverse('usermanage.addPerson'))
	return json_response(ajaxData)