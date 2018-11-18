# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	# return HttpResponse("hello world!")
	context = {}
	context['hello'] = 'Hello WORLD!'
	return render(request,'hello.html',context)