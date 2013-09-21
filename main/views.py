from django.http import HttpResponse
from django_facebook.models import FacebookProfile

def index(request):
	if not request.user.is_authenticated():
		return render_to_response('index.html', {'logged_in': 0}, context_instance=RequestContext(request))
	else:
		return render_to_response('index.html', {'logged_in': 1}, context_instance=RequestContext(request))

