# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import logout as user_logout
from forms import LoginForm
from ticketsystem.views import view_dashboard


def loginview(request):
    state=_("Enter Username and Password...")
    username=password=''
    form = LoginForm()
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            state = _("Login is Successful")
            return HttpResponseRedirect("/ticketsystem/mytickets")
        state = _("Invalid Username or Password!!")
    return render_to_response('userprofile/index.html', {'form':form,'state':state})

def logout(request):
    user_logout(request)
    return HttpResponseRedirect(reverse("loginview"))
