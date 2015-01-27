# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'11', verbose_name='Department')),
                ('depadmin', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('followupnote', models.CharField(max_length=1000, verbose_name='Comment')),
                ('followup_date', models.DateTimeField(null=True, verbose_name='Modified Date', blank=True)),
                ('assigned_user', models.ForeignKey(related_name='Assigned User', verbose_name='Assign to', to=settings.AUTH_USER_MODEL)),
                ('followup_user', models.ForeignKey(related_name='followup_user', verbose_name='Comment by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'15', verbose_name='Priority')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Product')),
                ('department', models.ForeignKey(to='ticketsystem.Department')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'15', verbose_name='Status')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created Date')),
                ('createdbyUser', models.ForeignKey(related_name='createdbyuser', verbose_name='Creator', to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(verbose_name='Department', to='ticketsystem.Department')),
                ('priority', models.ForeignKey(verbose_name='Priority', to='ticketsystem.Priority')),
                ('product', models.ForeignKey(verbose_name='Product', to='ticketsystem.Product')),
                ('status', models.ForeignKey(verbose_name='Status', to='ticketsystem.Status')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='followup',
            name='ticket',
            field=models.ForeignKey(to='ticketsystem.Ticket'),
            preserve_default=True,
        ),
    ]
