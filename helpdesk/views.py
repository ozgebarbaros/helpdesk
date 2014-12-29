# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response

from helpdesk.models import Ticket
from helpdeskforms import CreateTicketForm


@login_required
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
        return render_to_response('createticket.html', {'form':form,'status':status})

@login_required
def view_dashboard(request):
    tickets = Ticket.objects.filter(createdbyUser=request.user)
    return render_to_response('homepage.html', {'tickets':tickets})

def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/accounts/login")
    else:
        return HttpResponseRedirect("/dashboard")

