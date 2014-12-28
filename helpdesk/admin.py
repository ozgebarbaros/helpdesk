#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from helpdesk.models import Department, Product, Status, Priority

class DepartmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Department, DepartmentAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class StatusAdmin(admin.ModelAdmin):
    pass
admin.site.register(Status, StatusAdmin)

class PriorityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Priority, PriorityAdmin)