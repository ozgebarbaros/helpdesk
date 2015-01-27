from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('ticketsystem.views',
    url(r'^show/(?P<ticket_id>[0-9]+)', "showticket", name="showticket"),
    url(r'^mytickets/', "view_dashboard", name="view_dashboard"),
    url(r'^ticketcreate', 'createTicket', name='createTicket'),
    url(r'^assigned', 'assignedtome', name='assignedtome'),
    url(r'^update/(?P<ticket_id>[0-9]+)', 'updateticket', name='updateticket'),
)
