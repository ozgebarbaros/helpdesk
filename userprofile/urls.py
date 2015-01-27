from django.conf.urls import patterns, url, include

urlpatterns = patterns('userprofile.views',
    # Examples:
    # url(r'^$', 'helpdesk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login', 'loginview', name="loginview"),
    url(r'^logout', 'logout', name="logout"),

)
