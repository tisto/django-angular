# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0015_auto_20151008_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='end_date',
            field=models.DateField(help_text='End date needs to be after start date.', auto_now=True, verbose_name='End date', null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='start_date',
            field=models.DateField(help_text='Start date needs to be before end date.', auto_now=True, verbose_name='Start date', null=True),
        ),
    ]
