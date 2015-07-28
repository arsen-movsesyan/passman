# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountAttributeModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('acct_value', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'account_attribute',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('attribute_name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'db_table': 'attribute',
                'managed': False,
            },
        ),
    ]
