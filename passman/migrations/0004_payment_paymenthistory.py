# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passman', '0003_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('acct', models.OneToOneField(related_name='payment', primary_key=True, db_column=b'acct_id', serialize=False, to='passman.Account')),
                ('due_date_day', models.IntegerField(blank=True)),
                ('due_date_condition', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('payment_amount', models.CharField(max_length=255)),
                ('confirmation_code', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'payment_history',
                'managed': False,
            },
        ),
    ]
