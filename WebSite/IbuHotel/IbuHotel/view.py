from django.http import HttpResponse
from django.shortcuts import render,render_to_response


def index(request):
    return HttpResponse("Hello world!")

def hello(request):
    context = {}
    context['hello'] = 'Hello World! v2'
    return render(request, 'hello.html', context)

def page_404(request):
	# return render(request,'404.html')
	return render_to_response('404.html')

def page_500(request):
	return render(request,'500.html')