#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
#STATUS = (
#    (1, ("OPEN")),
#    (2, ("REOPEN")),
#    (3, ("RESOLVED")),
#    (4, ("CLOSED"))
#)
class Status(models.Model):
    name= models.CharField(max_length="15")
    def __unicode__(self):
       return self.name

#PRIORITY = (
#    (1, "CRITICAL"),
#    (2, "HIGH"),
#    (3, "NORMAL"),
#    (4, "LOW"),
#)

class Priority(models.Model):
    name= models.CharField(max_length="15")
    def __unicode__(self):
       return self.name

# TODO 
#User needs to be add to Department model
class Department(models.Model):
    name = models.CharField(max_length="11")
    def __unicode__(self):
	   return self.name

# TODO
# product model can extensible
class Product(models.Model):
    #product name can be (database, internet domain, email)
    name = models.CharField(max_length = 50)
    department = models.ForeignKey(Department)
    def __unicode__(self):
        return self.name
    
# TODO
#resolution and assignee can be add    
class Ticket(models.Model):
    product = models.ForeignKey(Product)
    department = models.ForeignKey(Department)
    status = models.ForeignKey(Status)
    priority = models.ForeignKey(Priority)
    followUpUser= models.ForeignKey(User,related_name='followupuser')
    createdbyUser= models.ForeignKey(User,related_name='createdbyuser')
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    created_date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(blank=True)
    comment= models.CharField(max_length = 1000)

