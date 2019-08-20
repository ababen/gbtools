import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .models import Expenses

def index(request):
		return HttpResponse("Hello, World!")


def list(request):
	try:
		expenses = Expenses.objects.all()
	except Expenses.DoesNotExists:
		raise Http404("Expenses do not exist!")
		return 


def add(request):
    if request.method == 'POST':
    	# Do something
    return