# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('f_name', models.CharField(max_length=255)),
                ('l_name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('ssn_13', models.CharField(max_length=3)),
                ('ssn_45', models.CharField(max_length=3)),
                ('ssn_69', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'ssn',
                'managed': False,
            },
        ),
    ]
