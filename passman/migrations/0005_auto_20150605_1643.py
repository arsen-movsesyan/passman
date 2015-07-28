# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passman', '0004_payment_paymenthistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymenthistory',
            options={'ordering': ['payment_date'], 'managed': False},
        ),
    ]
