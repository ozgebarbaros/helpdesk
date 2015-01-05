#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models

class Department(models.Model):
    name = models.CharField(_("Department"), max_length="11")
    depadmin = models.ForeignKey(User)
    def __unicode__(self):
        return self.name

class Product(models.Model):
    #product name can be (database, internet domain, email)
    name = models.CharField(verbose_name=_("Product"), max_length = 50)
    department = models.ForeignKey(Department)
    def __unicode__(self):
        return self.name

class Status(models.Model):
    name= models.CharField(verbose_name=_("Status"), max_length="15")
    def __unicode__(self):
        return self.name

class Priority(models.Model):
    name= models.CharField(verbose_name=_("Priority"), max_length="15")
    def __unicode__(self):
        return self.name

class Ticket(models.Model):
    product = models.ForeignKey(Product,verbose_name=_("Product"))
    department = models.ForeignKey(Department,verbose_name=_("Department"))
    status = models.ForeignKey(Status,verbose_name=_("Status"))
    priority = models.ForeignKey(Priority,verbose_name=_("Priority"))
    followUpUser= models.ForeignKey(User,related_name='followupuser',verbose_name=_("Assigned User"))
    createdbyUser= models.ForeignKey(User,related_name='createdbyuser',verbose_name=_("Creator"))
    title = models.CharField(verbose_name=_("Title"), max_length = 100)
    description = models.CharField(verbose_name=_("Description"), max_length = 1000)
    created_date = models.DateTimeField(verbose_name=_("Created Date"), default=datetime.now)
    modified_date = models.DateTimeField(verbose_name=_("Modified Date"), blank=True, null=True)

class Comment(models.Model):
    comment= models.CharField(verbose_name=_("Comment"), max_length = 1000)
    ticket= models.ForeignKey(Ticket)



