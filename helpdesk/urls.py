from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from helpdesk.views import loginview

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helpdesk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
)

urlpatterns+=patterns('helpdesk.views',
    url(r'^$','loginview', name='loginview')
)

from django.conf import settings

urlpatterns += staticfiles_urlpatterns()