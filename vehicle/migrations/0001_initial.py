# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('v_make', models.CharField(max_length=255)),
                ('v_model', models.CharField(max_length=255)),
                ('v_year', models.CharField(max_length=4)),
                ('vin', models.CharField(max_length=255)),
                ('license_plate', models.CharField(max_length=255)),
                ('purchase_date', models.DateField()),
                ('nonoperational_date', models.DateField()),
            ],
            options={
                'managed': False,
            },
        ),
    ]
