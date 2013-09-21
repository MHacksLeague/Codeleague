from django.shortcuts import render

def index(request):
	context = {'logged_in': 0}
	return render(request, 'index.html', context)
