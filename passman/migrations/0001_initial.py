# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('acct_name', models.CharField(unique=True, max_length=255)),
                ('login', models.CharField(max_length=255)),
                ('passwd', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['created_at'],
                'db_table': 'acct',
                'managed': False,
            },
        ),
    ]
