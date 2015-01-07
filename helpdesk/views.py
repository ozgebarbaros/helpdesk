# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User, Group
from helpdesk.models import *
from helpdeskforms import CreateTicketForm, UpdateFollowUpForm 



@login_required
def createTicket(request):
    if request.user.is_authenticated():
        status = _("Fill Form")
        initialdata={'status':'1'}
        if request.POST:
            department=Product.objects.get(pk=request.POST['product']).department
            initialdata['department']=department.pk
            initialdata['createdbyUser']=request.user.id
            initialdata['product']=request.POST['product']
            initialdata['priority']=request.POST['priority']
            initialdata['title']=request.POST['title']
            initialdata['description']=request.POST['description']
            initialdata['created_date']=datetime.now()
            form=CreateTicketForm(initialdata)
            if form.is_valid():
                try:
                    new_ticket=form.save(commit=True)
                    new_followup=FollowUp(ticket=new_ticket,followup_user=request.user,assigned_user=department.depadmin,followup_date=initialdata['created_date'],followupnote=_('This issue assigned to your department'))
                    new_followup.save()
                    status = _("Form Saved")
                except Exception as e:
                    status = _("Error Occured")
                    print e
            else:
                print _("Form Couldn't Be Saved")
        else:
            form = CreateTicketForm()
        return render_to_response('createticket.html', {'form':form,'status':status})

@login_required
def view_dashboard(request):
    tickets = Ticket.objects.filter(createdbyUser=request.user)
    return render_to_response('mytickets.html', {'tickets':tickets})

@login_required
def showticket(request,ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    return render_to_response('ticketdetails.html',{'ticket':ticket})

@login_required
def updateticket(request,ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    followups = FollowUp.objects.filter(ticket=ticket_id)
    initialdata={'ticket':ticket_id}
    if request.POST:
        initialdata['followupnote']=request.POST['followupnote']
        initialdata['followup_date']=datetime.now()
        initialdata['followup_user']=request.user.id
        if request.POST['assigned_user'] != '':
	    initialdata['assigned_user']=request.POST['assigned_user']
        else:
            initialdata['assigned_user']=request.user.id
        form=UpdateFollowUpForm(initialdata)
        if form.is_valid():
            form.save(commit=True)
    else:
        form=UpdateFollowUpForm()
    return render_to_response('updateticket.html',{'ticket':ticket,'followups':followups,'form':form})

@login_required
def assignedtome(request):
    followups = FollowUp.objects.filter(assigned_user=request.user.pk)
    tickets=[]
    for followup in followups:
        tickets.append(followup.ticket)
    return render_to_response('assignedtome.html',{'tickets':set(tickets)})

def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/accounts/login")
    else:
        return HttpResponseRedirect(reverse("view_dashboard"),{'user':request.user})

