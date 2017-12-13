# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-13 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbaack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=30)),
                ('contact_email', models.EmailField(max_length=254, unique=True)),
                ('content', models.CharField(max_length=500)),
                ('ip_add', models.CharField(default='ABC', max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
