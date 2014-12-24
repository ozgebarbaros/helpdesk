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
    if request.POST:
        print "hede"
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                state="Giris basarili!"
                return render_to_response('homepage.html')
            state = "Kullanici adi veya parola hatali!!"
        
    else:
         form = LoginForm()
    
    data = {
                 'form': form,
    }
    
    return render_to_response('index.html', data)