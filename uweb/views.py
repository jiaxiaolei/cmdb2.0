# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
 
def index(request):
    return HttpResponse(u"Welcome to cmdb2.0!")

def test(request):
    ret = dict(code=0,
               message='success',
               data={})
    return JsonResponse(ret)
