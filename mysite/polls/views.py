#coding:utf-8
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question,Choise
from django.core.urlresolvers import reverse
from django.template import RequestContext,loader

# Create your views here.


def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]


    """template=loader.get_template('polls/index.html')
    context=RequestContext(request,{
        'latest_question_list':latest_question_list,
    })
    """
    #output=','.join([p.question_text for p in latest_question_list])

    context={'latest_question_list':latest_question_list}
    #return HttpResponse(template.render(context))

    return render(request,'polls/index.html',context)
    #   render()函数将请求对象作为它的第一个参数，模板的名字作为它的第二个参数，一个字典作为它可选的第三个参数。 它返回一个HttpResponse对象，含有用给定的context 渲染后的模板

def detail(request,question_id):

    """
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("question does not exit!")
    """
    question=get_object_or_404(Question,pk=question_id)

    return render(request,'polls/detail.html',{'question':question})
    #return HttpResponse('you are look at question %s.'%question_id)

def results(request,question_id):

    question=get_object_or_404(Question,question_id)

    return render(request,'polls/results.html',{'question':question})



def vote(request,question_id):
    p=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=p.choise_set.get(pk=request.POST['choice'])
    except (KeyError,Choise.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':p,
            'error_message':"you didn't select a choice!",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id)))


        #return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
