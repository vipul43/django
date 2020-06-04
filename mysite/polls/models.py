#NOTE:
#   WHENEVER YOU MAKE A CHANGE IN THE METHODS OF THE CLASSES IN THIS FILE
#   AND YOU WANT TO PLAY WITH THE DJANGO DB API
#   EXIT THE SHELL AND REENTER


from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return '{}'.format(self.question_text)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    #models.ForeignKey() is used to mention the relationship between choice and question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return 'choice: {}, votes: {}'.format(self.choice_text, self.votes)
