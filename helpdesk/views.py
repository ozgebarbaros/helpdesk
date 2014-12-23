# -*- coding: utf-8 -*-

from django.views.generic import View, DetailView, TemplateView, ListView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.template.context import RequestContext


def loginview(request):
    state="Kullanici adini giriniz..."
    username=password=''
    if request.POST:
        print "hede"
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            state="Giris basarili!"
            return render_to_response('index.html',{'state':state, 'username':username})
        state = "Kullanici adi veya parola hatali!!"
    return render_to_response('index.html',{'state':state, 'username':username})