#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

STATUS = (
    (1, ("OPEN")),
    (2, ("REOPEN")),
    (3, ("RESOLVED")),
    (4, ("CLOSED"))
)

PRIORITY = (
    (1, "CRITICAL"),
    (2, "HIGH"),
    (3, "NORMAL"),
    (4, "LOW"),
)

# TODO 
#User needs to be add to Department model
class Department(models.Model):
    name = models.CharField()

# TODO
# product model can extensible
class Product(models.Model):
    #product name can be (database, internet domain, email)
    name = models.CharField(max_length = 50)
    department = models.ForeignKey(Department)
    
# TODO
#resolution and assignee can be add    
class Ticket(models.Model):
    product = models.ForeignKey(Product) 
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    priority =  models.IntegerField (choices = PRIORITY)
    created_date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(blank=True)
    status =  models.IntegerField(choices = STATUS)
    

