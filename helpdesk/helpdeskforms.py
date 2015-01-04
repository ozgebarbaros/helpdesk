#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.forms import ModelForm

from helpdesk.models import Ticket


class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['department', 'status', 'createdbyUser', 'created_date']
        
        
class UpdateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = {}