# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0009_auto_20150904_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='title',
            field=models.CharField(default='My first application', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(blank=True, max_length=6, null=True, choices=[(b'm', b'male'), (b'f', b'female')]),
        ),
    ]
