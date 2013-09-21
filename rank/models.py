from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	school = models.CharField(max_length=30)
	github = models.CharField(max_length=30)
	# rank = property(get_rank)
	

	def get_score():
		total_score = 0

		results = Result.objects.filter(user_profile=self.id)

		for result in results:
			total_score += result.score

		return total_score

	score = property(get_score)
	# def get_rank:


class Hackathon(models.Model):
	name = models.CharField(max_length=30)


class Result(models.Model):
	user_profile = models.ForeignKey(UserProfile)
	hackathon = models.ForeignKey(Hackathon)
	rank = models.IntegerField()
	score = models.IntegerField()