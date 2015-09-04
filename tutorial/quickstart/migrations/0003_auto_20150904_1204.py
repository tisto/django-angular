# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20150904_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='date',
            field=models.DateField(default=None),
        ),
    ]
