# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0012_auto_20150918_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='salutation',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Salutation', choices=[(b'mr', b'Mr'), (b'mrs', b'Mrs'), (b'ms', b'Ms')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='zip_number',
            field=models.CharField(max_length=5, null=True, verbose_name='ZIP number'),
        ),
    ]
