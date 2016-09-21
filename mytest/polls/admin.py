#coding:utf-8
from django.contrib import admin

# Register your models here.
from .models import Qusetion,Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question_text']
    fieldsets = [
        ('问题汇总',{'fields':['question_text']}),
        ('时间信息',{'fields':['pub_date']}),
    ]

    inlines =[ChoiceInLine]

    list_display = ('question_text', 'pub_date','was_published_recently')

    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 20#20条分页
    #date_hierarchy = 'pub_date'

admin.site.register(Qusetion,QuestionAdmin)