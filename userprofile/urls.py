from django.conf.urls import patterns, url

urlpatterns = patterns('userprofile.views',
    url(r'^login', 'loginview', name="loginview"),
    url(r'^logout', 'logout', name="logout"),
)
