from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
   
   #user auth urls
    url(r'^login/$', 'mysite.views.login'),
    url(r'^auth/$', 'mysite.views.auth_view'),
    url(r'^logout/$', 'mysite.views.logout'),
    url(r'^loggedin/$', 'mysite.views.loggedin'),
    url(r'^invalid/$', 'mysite.views.invalid_login'),
    url(r'^register/$', 'mysite.views.register_user'),
    url(r'^register_success/$', 'mysite.views.register_success'),
)
