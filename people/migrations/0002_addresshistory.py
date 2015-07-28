# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('str_address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=5)),
                ('comments', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'address_history',
                'managed': False,
            },
        ),
    ]
