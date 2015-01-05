from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('helpdesk.views',
    # Examples:
    # url(r'^$', 'helpdesk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', "index", name="index"),
    url(r'^accounts/', include('userprofile.urls')),
    url(r'^show/(?P<ticket_id>[0-9]+)', "showticket", name="showticket"),
    url(r'^mytickets/', "view_dashboard", name="view_dashboard"),
    url(r'^ticketcreate', 'createTicket', name='createTicket'),
    url(r'^assigned', 'assignedtome', name='assignedtome'),
    url(r'^update/(?P<ticket_id>[0-9]+)', 'updateticket', name='updateticket'),
    url(r'^admin/', include(admin.site.urls)),
)
