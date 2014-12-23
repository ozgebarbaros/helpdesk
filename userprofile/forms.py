# -*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))