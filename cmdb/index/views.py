# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework.response import Response

from django.http import HttpResponse

from rest_framework.response import Response

def index(request):
    return HttpResponse(u"Welcome to cmdb2.0!")
