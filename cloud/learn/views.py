from django.shortcuts import render
#coding:utf-8
from django.http import HttpResponse

def index(request):
    return HttpResponse(u"welcome to my learn")


def home(request):
    return render(request,'index.jsp')



