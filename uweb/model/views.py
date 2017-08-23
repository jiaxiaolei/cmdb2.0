# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.response import Response

from rest_framework.decorators import api_view

from django.contrib.auth.models import User, Group

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

# Create your views here.

class ListUsers(APIView):
    """ 
    View to list all users in the system.  
    * Requires token authentication.  
    * Only admin users are able to access this view.  
    """ 
    #authentication_classes = (authentication.TokenAuthentication,) 
    #permission_classes = (permissions.IsAdminUser,) 
    
    def get(self, request, format=None): 
        """ Return a list of all users.  """ 
        usernames = ['test', 'in', 'module'] 
        #usernames = [user.username for user in User.objects.all()] 
        return Response(usernames)

    def post(self, request, format=None): 
        usernames = ['test', 'in', 'module post'] 
        return Response(usernames)

    def put(self, request, format=None): 
        usernames = ['test', 'in', 'module put'] 
        return Response(usernames)

    def delete(self, request, format=None): 
        usernames = ['test', 'in', 'module delete'] 
        return Response(usernames)


