#coding:utf-8

from django.db import models
import datetime

from django.utils import timezone

# Create your models here.


class Qusetion(models.Model):
    question_text=models.CharField('问题',max_length=200)
    pub_date=models.DateTimeField('时间')

    def __unicode__(self):
        return self.question_text


    def was_published_recently(self):
        return self.pub_date >=timezone.now()-datetime.timedelta(days=1)

    was_published_recently.short_description='是否'
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True

class Choice(models.Model):
    question=models.ForeignKey(Qusetion)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text



