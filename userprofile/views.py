# -*- coding: utf-8 -*-
from django.views.generic import View, DetailView, TemplateView, ListView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.template.context import RequestContext

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
            return render_to_response('homepage.html')
        state = "Kullanici adi veya parola hatali!!"
    return render_to_response('index.html', {'form':form,'state':state})
