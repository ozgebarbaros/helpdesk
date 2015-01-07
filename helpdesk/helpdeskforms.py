#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.models import User
from helpdesk.models import Ticket,FollowUp


class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude={}
        widgets={
                 'department':forms.HiddenInput(),
                 'status':forms.HiddenInput(),
                 'createdbyUser':forms.HiddenInput(),
                 'created_date':forms.HiddenInput(),
		 'description':forms.Textarea(),
            }

class UpdateFollowUpForm(ModelForm):
    assigned_user = ModelChoiceField(queryset=User.objects.none(),label="* Bölüm") #Jquery ile uretilecek burasi
    class Meta:
        model = FollowUp
        exclude = {}
        widgets={
            'followupnote':forms.Textarea(),
            'ticket':forms.HiddenInput(),
	    'followup_date':forms.HiddenInput(),
            'followup_user':forms.HiddenInput(),
        }
