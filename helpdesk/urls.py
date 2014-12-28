from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('helpdesk.views',
    # Examples:
    # url(r'^$', 'helpdesk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('userprofile.urls')),
    url(r'^dashboard', "view_dashboard", name="view_dashboard"),
    url(r'^ticketcreate', 'createTicket',name='createTicket'),
    url(r'^admin/', include(admin.site.urls)),
)