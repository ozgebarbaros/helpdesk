# -*- coding: utf-8 -*-

from django.views.generic import View, DetailView, TemplateView, ListView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.template.context import RequestContext
from helpdeskforms import CreateTicketForm
from django.db.transaction import commit

def createTicket(request):
    if request.user.is_authenticated():
        status="Formu doldur"
        if request.POST:
            form = CreateTicketForm(request.POST)
            try:
               print form
               form.save(commit=True)
               status="form kaydedildi"
            except Exception as e:
               status="hata olustu"
               print e
        else:
            form = CreateTicketForm()
        return render_to_response('createticket.html',{'form':form,'status':status})