from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('helpdesk.views',
    url(r'^$', "index", name="index"),
    url(r'^accounts/', include('userprofile.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ticketsystem/', include('ticketsystem.urls')),
)
