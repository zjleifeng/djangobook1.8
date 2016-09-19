#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/19 17:24
# @Author  : Aries
# @Site    :
# @File    : 11.py
# @Software: PyCharm

from django.contrib import admin
from .models import Question,Choise

# Register your models here.

class ChoiseInLine(admin.TabularInline):
    model = Choise
    extra = 3

"""
无论何时，当你需要修改一个对象的管理选项的话，就按照这样的步骤来做：
创建一个模型管理对象（class），然后把该对象（class名）作为第二个参数传入admin.site.register()。
那特定的更改，使得“Publication date”字段排在“Question”字段前面：

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)


"""


"""
仅有两个字段不会令你印象深刻，但是当管理有许多字段的表单时，选择一个直观的排序方式是一个重要而实用的细节。

说到有许多字段的表单，你可能想把表单分割成字段集：


fieldsets中每个元组的第一个元素是字段集的标题。

你可以任意地为每个字段集指定HTML样式类。
"""


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']#这行代码添加一个“Filter”侧边栏，可以使人们通过pub_date字段对变更列表进行过滤：
    search_fields = ['question_text']#搜索功能：
    list_display = ('question_text', 'pub_date', 'was_published_recently')#它是一个要显示的字段名称的元组，在对象的变更列表页面上作为列显示：
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiseInLine]

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choise)




