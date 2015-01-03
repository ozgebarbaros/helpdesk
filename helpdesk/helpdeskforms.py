#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from helpdesk.models import Ticket

class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude={'followUpUser','comment','modified_date'}
        widgets={
            'department':forms.HiddenInput(),
            'status':forms.HiddenInput(),
            'createdbyUser':forms.HiddenInput(),
            'created_date':forms.HiddenInput(),
        }
        
        
class UpdateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = {}