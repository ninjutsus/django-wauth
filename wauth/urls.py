__author__ = 'wils0n'

from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

	url(r'^$', BaseView.as_view(), name='auth_login'),
	url(r'^auth/login/external/$', LoginExternalView.as_view(), name='auth_login_external'),
	url(r'^auth/logout/$', 'wauth.views.logout_view', name='auth_logout'),
	url(r'^auth/login/$', 'wauth.views.login_view', name='auth_login'),
)
