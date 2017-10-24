from django.db import models
from django.utils import timezone

from datetime import datetime, timedelta

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)

	correct = models.BooleanField(default=False)
	
	def __str__(self):
		return self.choice_text
		
class User(models.Model):
	user_name = models.CharField(max_length=100)
	user_id = models.IntegerField(primary_key=True)
	user_fio = models.CharField(max_length=100)
	time =  models.IntegerField(default=40)
	kol_quest = models.IntegerField(default=10)
	corr_ans = models.IntegerField(default=0)
	quest_now = models.IntegerField(default=0)
	time_begin = models.DateTimeField(auto_now_add=True)
	time_end = models.DateTimeField(auto_now_add=True)




	def __str__(self):
		return self.user_name