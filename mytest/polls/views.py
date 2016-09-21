from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Qusetion,Choice
# Create your views here.

def index(request):
    latest_question_list=Qusetion.objects.all()
    context={'latest_question_list':latest_question_list}
    return render(request,'polls/index.heml',context)



def detail(request,question_id):
    question=get_object_or_404(Qusetion,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})


def results(request,question_id):
    question=get_object_or_404(Qusetion,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request,question_id):
    p=get_object_or_404(Qusetion,pk=question_id)
    try:
        select_choice=p.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':p,
            'error_message':"you didn't select a choice!",
        })
    else:
        select_choice.votes+=1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(p.id)))

