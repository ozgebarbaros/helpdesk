# -*- coding: utf-8 -*-

from django.http.response import HttpResponseRedirect

def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/accounts/login")
    else:
        print request.user
        return HttpResponseRedirect("/ticketsystem/mytickets",{'user':request.user})
