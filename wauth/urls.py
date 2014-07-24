__author__ = 'wils0n'

from django.conf.urls import patterns, include, url
from .views import *
from django.views.generic import *

urlpatterns = patterns('',
                       url(r'^$', BaseView.as_view(), name='auth_login'),
                       url(r'^auth/login/external/$', LoginExternalView.as_view(), name='auth_login_external'),
                       url(r'^auth/logout/$', 'wauth.views.logout_view', name='auth_logout'),
                       url(r'^auth/login/$', 'wauth.views.login_view', name='auth_login'),
                       url(r'^sandbox/test/$', TemplateView.as_view(template_name='wauth/test.html')),
                       )
