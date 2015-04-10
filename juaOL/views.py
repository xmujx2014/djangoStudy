from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from usermanage.models import User
def index(request):
	# return HttpResponse('ok')
	return render(request, 'index.html')

@require_http_methods(['POST'])
@csrf_exempt
def jua_login(request):
	username = request.POST.get('username', '')
	passwd = request.POST.get('password', '')
	print '%s:%s' % (username, passwd)
	user = authenticate(username=username, password=passwd)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/sysadmin/')
			# return render(request, 'admin.html', {'value': 'Hello: %s' % request.user.username})
	else:
		com_user = User.objects.get(username=username)
		if com_user.passwd == passwd:
			return HttpResponseRedirect('/usermanage/')
			# return render(request, '/usermanage/')
	return render(request, 'index.html')
