#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

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
    name = models.CharField(max_length="11")
    depadmin = models.ForeignKey(User)
    def __unicode__(self):
        return self.name

class Product(models.Model):
    #product name can be (database, internet domain, email)
    name = models.CharField(max_length = 50)
    department = models.ForeignKey(Department)
    def __unicode__(self):
        return self.name

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
# product model can extensible

class Comment(models.Model):
    comment= models.CharField(max_length = 1000,verbose_name="Yorum")

# TODO
#resolution and assignee can be add    
class Ticket(models.Model):
    product = models.ForeignKey(Product,verbose_name='Servis')
    department = models.ForeignKey(Department,verbose_name='Bolum')
    status = models.ForeignKey(Status,verbose_name='Durum')
    priority = models.ForeignKey(Priority,verbose_name='Oncelik')
    followUpUser= models.ForeignKey(User,related_name='followupuser')
    createdbyUser= models.ForeignKey(User,related_name='createdbyuser')
    title = models.CharField(max_length = 100,verbose_name="Baslik")
    description = models.CharField(max_length = 1000,verbose_name="Aciklama")
    created_date = models.DateTimeField(default=datetime.now,verbose_name="Olusturulma Tarihi")
    modified_date = models.DateTimeField(blank=True, null=True,verbose_name="Degistirilme Tarihi")
    comment= models.ForeignKey(Comment,blank=True,null=True)

