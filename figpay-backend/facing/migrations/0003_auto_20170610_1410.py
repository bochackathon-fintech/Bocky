# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-10 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_consumer_image_1'),
        ('facing', '0002_remove_upload_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='recognized_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paying_uploads', to='profiles.Vendor'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='originating_uploads', to='profiles.Vendor'),
        ),
    ]
