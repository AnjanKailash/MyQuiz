import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
	category_name = models.CharField(max_length = 25)
	def __unicode__(self):
		return self.category_name

class Question(models.Model):
	category = models.ForeignKey(Category)
	question_text = models.CharField(max_length = 200, unique = True, null = False)
	correct_choice = models.CharField(max_length = 30, null = False)
	pub_date = models.DateTimeField('date published', auto_now_add = True, auto_now = False)
	marks = models.IntegerField(default=1)
	author = models.CharField(max_length = 40, null = False)
	def __unicode__(self):
		return self.question_text
	def was_published_recently(self):
	    now = timezone.now()
	    return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
    
class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length = 30, null = False)
	correctness = models.BooleanField(default = False)
	def __unicode__(self):
		return self.choice_text

