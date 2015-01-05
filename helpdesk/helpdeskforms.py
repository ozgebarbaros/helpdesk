#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm

from helpdesk.models import Ticket,Comment


class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude={'comment','modified_date'}
        widgets={
                 'department':forms.HiddenInput(),
                 'status':forms.HiddenInput(),
                 'createdbyUser':forms.HiddenInput(),
                 'created_date':forms.HiddenInput(),
		         'followUpUser':forms.HiddenInput(),
                 'description':forms.Textarea(),
            }
             
class UpdateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = {}

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = {}
        widgets={
            'comment':forms.Textarea(),
            'ticket':forms.HiddenInput(),
        }