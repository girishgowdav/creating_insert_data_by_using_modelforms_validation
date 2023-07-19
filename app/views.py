from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    TMFO=TopicModelForm()
    d={'TMFO':TMFO}
    if request.method=='POST':
        TMFD=TopicModelForm(request.POST)
        if TMFD.is_valid():
            TMFD.save()
            return HttpResponse('data is inserted')
    return render(request,'insert_topic.html',d)



def insert_webpage(request):
    WMFO=WebpageModelForm()
    d={'WMFO':WMFO}
    if request.method=='POST':
        WMFD=WebpageModelForm(request.POST)
        if WMFD.is_valid():
            WMFD.save()
            return HttpResponse('webpage is inserted')

    return render(request,'insert_webpage.html',d)


def insert_accessrecords(request):
    ARMFO=AccessRecordsModelForm()
    d={'ARMFO':ARMFO}
    if request.method=='POST':
        ARMFD=AccessRecordsModelForm(request.POST)
        if ARMFD.is_valid():
            ARMFD.save()
            return HttpResponse('accessrecords is inserted')

    return render(request,'insert_accessrecords.html',d)
