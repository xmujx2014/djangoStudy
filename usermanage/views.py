from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import Person

# Create your views here.

def teaminfo(request):
	values = request.META.items()
	values.sort()
	html = []
	# for k, v in values:
	# 	html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	# return HttpResponse("<table>%s</table>" % '\n'.join(html))
	return render(request, 'user_manage.html')

def addPerson(request):
	attrs = ['team', 'family_name', 'given_name', 'simple_name',
		'identity_num', 'gender', 'groupe', 'category']
	personInfo = Person()
	# personInfo.id = 1
	# personInfo.team = 'e'
	# setattr(personInfo, 'team', 'h')
	person_str = '{'
	for attr in attrs:
		setattr(personInfo, attr, request.POST.get(attr, ''))
	# 	personInfo.attr = request.POST.get(attr, 'NULL')
		person_str += '%s : %s; \n' % (attr, getattr(personInfo, attr))
	personInfo.save()
	# return HttpResponse("<table></table>")
	return render(request, 'user_manage.html', {'str': person_str})