# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0013_auto_20150922_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='country',
            field=models.CharField(max_length=255, null=True, verbose_name='Country'),
        ),
    ]
