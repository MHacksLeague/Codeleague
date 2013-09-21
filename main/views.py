from django.shortcuts import render
from django_facebook.models import FacebookProfile

def index(request):
	context = {'logged_in': 0}
	return render(request, 'index.html', context)
