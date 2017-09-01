"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from cmdb.index import views as cmdb_views 
#from cmdb import views as cmdb_views 
from cmdb.model import views as model_views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', cmdb_views.index), 
    #url(r'^test/', cmdb_views.test), 

    #url(r'list/$', cmdb_views.ListUsers.as_view()),
    #url(r'^cmdb/api/model/$', model_views.ListUsers.as_view()),
    
    #url(r'^admin/', admin.site.urls),

    # NOUSED.
    #url(r'^cmdb/api/', include('uweb.urls')),

    # graphiql
    url(r'^graphiql', include('django_graphiql.urls')),

    # rest_framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

# add static url
urlpatterns += staticfiles_urlpatterns()

