# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-10 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_fulfilled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='payment',
            name='response',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='type',
            field=models.CharField(choices=[('vi', 'Visa'), ('api', 'BoC API')], default='api', max_length=2),
        ),
    ]
