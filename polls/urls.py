from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	
	url(r'^$', views.IndexView.as_view(), name='index'),
	
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),

	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

	#user auth urls
  url(r'^login/$', 'polls.views.login'),
  url(r'^auth/$', 'polls.views.auth_view'),
  url(r'^logout/$', 'polls.views.logout'),
  url(r'^loggedin/$', 'polls.views.loggedin'),
  url(r'^invalid/$', 'polls.views.invalid_login'),
  url(r'^register/$', 'polls.views.register_user'),
  url(r'^register_success/$', 'polls.views.register_success'),
)