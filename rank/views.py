from django.shortcuts import render_to_response
from rank.models import *

def HackerProfile(request):
	c = {}

	# user_profile = UserProfile.objects.get(user=request.user)
	# c['user_profile'] = user_profile

	return render_to_response("profile.html", c)

def Ranking(request):
	c = {}

	user_profile = UserProfile.objects.get(user=request.user)
	c['user_profile'] = user_profile

	return render_to_response("static/ranking.html", c)