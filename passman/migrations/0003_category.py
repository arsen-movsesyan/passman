# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passman', '0002_accountattributemodel_attribute'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('category_name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
    ]
