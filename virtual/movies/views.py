#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello_world(request):
	"""	Vista que regresa un hello world"""
	return HttpResponse("hello_world")
	
