#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/19 17:24
# @Author  : Aries
# @Site    :
# @File    : 11.py
# @Software: PyCharm

from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


"""
Question对象具有一个question_text（问题）属性和一个publish_date（发布时间）属性。
Choice有两个字段：选择的内容和选择的得票统计。 每个Choice与一个Question关联。
"""
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'


class Choise(models.Model):
    question=models.ForeignKey(Question)
    choise_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __unicode__(self):
        return self.choise_text
