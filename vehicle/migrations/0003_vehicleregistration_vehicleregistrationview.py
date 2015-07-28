# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_auto_20150507_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleRegistration',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('registration_issue_date', models.DateField()),
                ('registration_expiration', models.DateField()),
            ],
            options={
                'db_table': 'vehicle_registration',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleRegistrationView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('v_make', models.CharField(max_length=255)),
                ('v_model', models.CharField(max_length=255)),
                ('v_year', models.CharField(max_length=4)),
                ('license_plate', models.CharField(max_length=255)),
                ('vin', models.CharField(max_length=255)),
                ('last_issue_date', models.DateField()),
                ('expiration_date', models.DateField()),
            ],
            options={
                'db_table': 'vehicle_registration_view',
                'managed': False,
            },
        ),
    ]
