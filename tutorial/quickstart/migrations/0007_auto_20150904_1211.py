# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0006_auto_20150904_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='first_time_application',
            field=models.NullBooleanField(),
        ),
    ]
