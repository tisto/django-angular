# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0007_auto_20150904_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='attachment',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='application',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(max_length=6, null=True, choices=[(b'm', b'male'), (b'f', b'female')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='application',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
