#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models


#STATUS = (
#    (1, ("OPEN")),
#    (2, ("REOPEN")),
#    (3, ("RESOLVED")),
#    (4, ("CLOSED"))
#)
# TODO 
#User needs to be add to Department model
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

#PRIORITY = (
#    (1, "CRITICAL"),
#    (2, "HIGH"),
#    (3, "NORMAL"),
#    (4, "LOW"),
#)

class Priority(models.Model):
    name= models.CharField(verbose_name=_("Priority"), max_length="15")
    def __unicode__(self):
        return self.name


# TODO
# product model can extensible

class Comment(models.Model):
    comment= models.CharField(verbose_name=_("Comment"), max_length = 1000)

# TODO
#resolution and assignee can be add    
class Ticket(models.Model):
    product = models.ForeignKey(Product)
    department = models.ForeignKey(Department)
    status = models.ForeignKey(Status)
    priority = models.ForeignKey(Priority)
    followUpUser= models.ForeignKey(User,related_name='followupuser', blank=True, null=True)
    createdbyUser= models.ForeignKey(User,related_name='createdbyuser')
    title = models.CharField(verbose_name=_("Title"), max_length = 100)
    description = models.CharField(verbose_name=_("Description"), max_length = 1000)
    created_date = models.DateTimeField(verbose_name=_("Created Date"), default=datetime.now)
    modified_date = models.DateTimeField(verbose_name=_("Modified Date"), blank=True, null=True)
    comment= models.ForeignKey(Comment, blank=True,null=True)

