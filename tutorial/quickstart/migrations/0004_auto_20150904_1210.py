# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20150904_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='date',
            field=models.DateField(),
        ),
    ]
