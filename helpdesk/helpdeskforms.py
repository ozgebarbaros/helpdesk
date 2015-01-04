#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from helpdesk.models import Ticket
from django.db.backends.sqlite3.introspection import field_size_re

class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['department', 'status', 'createdbyUser', 'created_date']
        
        
class UpdateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = {}