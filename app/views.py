from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    TFO=Topicforms()
    d={'form':TFO}
    if request.method=='POST':
        fd=Topicforms(request.POST)
        if fd.is_valid():
            tn=fd.cleaned_data['topic_name']
            T=Topic.objects.get_or_create(topic_name=tn)[0]
            T.save()
            return HttpResponse('topic inserted successfully')
    return render(request,'insert_topic.html',d)


def modelform_topic(request):
    TMF=Modelform_topic()
    d={'form':TMF}
    if request.method=='POST':
        mft=Modelform_topic(request.POST)
        if mft.is_valid():
            mft.save()
            return HttpResponse('topic inserted successfully by modelforms')
    return render(request,'modelform_topic.html',d)


def modelform_webpage(request):
    WMFO=Modelform_webpage()
    d={'form':WMFO}
    if request.method=='POST':
        mfw=Modelform_webpage(request.POST)
        if mfw.is_valid():
            mfw.save()
            return HttpResponse('webpage inserted successfully by modelsforms')
    return render(request,'modelform_webpage.html',d)


def modelform_access(request):
    MFA=Modelform_access()
    d={'form':MFA}
    if request.method=='POST':
        mfa=Modelform_access(request.POST)
        if mfa.is_valid():
            mfa.save()
            return HttpResponse('accessrecords inserted by modelsforms')
        
    return render(request,'modelform_access.html',d)