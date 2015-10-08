# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0016_auto_20151008_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='username',
            field=models.CharField(null=True, verbose_name='Username', help_text='External validation, anything but "Bob" is valid.', max_length=255),
        ),
    ]
