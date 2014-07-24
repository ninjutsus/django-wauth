from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

admin.autodiscover()

urlpatterns = patterns('',

	url(r'^$', BaseView.as_view(), name='auth_login'),
	url(r'^auth/login/external/$', LoginExternalView.as_view(), name='auth_login_external'),
	url(r'^auth/logout/$', 'views.logout_view', name='auth_logout'),
	url(r'^auth/login/$', 'views.login_view', name='auth_login'),
	url(r'^admin/', include(admin.site.urls)),
)
