# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-29 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0007_status_hood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='nickname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='bio',
            name='user_bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='bio',
            name='user_hood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.Hood'),
        ),
    ]
