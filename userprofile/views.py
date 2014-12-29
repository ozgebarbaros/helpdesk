# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import logout as user_logout
from forms import LoginForm


def loginview(request):
    state="Kullanici adini giriniz..."
    username=password=''
    form = LoginForm()
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            state="Giris basarili!"
            return HttpResponseRedirect(reverse("view_dashboard"))
        state = "Kullanici adi veya parola hatali!!"
    return render_to_response('index.html', {'form':form,'state':state})

def logout(request):
    user_logout(request)
    return HttpResponseRedirect(reverse("loginview"))
