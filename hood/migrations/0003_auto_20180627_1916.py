# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-27 16:16
from __future__ import unicode_literals

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_auto_20180627_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='address',
        ),
        migrations.RemoveField(
            model_name='business',
            name='location',
        ),
        migrations.AddField(
            model_name='bio',
            name='address',
            field=django_google_maps.fields.AddressField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bio',
            name='location',
            field=django_google_maps.fields.GeoLocationField(blank=True, max_length=100),
        ),
    ]