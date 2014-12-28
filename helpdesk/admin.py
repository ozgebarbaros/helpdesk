#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from helpdesk.models import Department

class DepartmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Department, DepartmentAdmin)
