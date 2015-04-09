from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

def index(request):
	# return HttpResponse('ok')
	return render(request, 'index.html')

@require_http_methods(['POST'])
@csrf_exempt
def login(request):
	value = ''
	if 'username' in request.POST:
		value = request.POST['username']
	return render(request, 'admin.html',{'value': value})
	# return HttpResponse("ok")