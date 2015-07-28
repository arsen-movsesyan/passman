# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_addresshistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addresshistory',
            options={'ordering': ['start_date'], 'managed': False},
        ),
    ]
