from django.db import models

# Create your models here.
class Question(models.Model):
	question_text=models.CharField(max_length=200)
	question_date=models.DateTimeField('date published')
class Answer(models.Model):
	question=models.ForeignKey(Question)
	answer_text=models.CharField(max_length=1000)
	votes=models.IntegerField(default=0)
	answer_date=models.DateTimeField('date published')