# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('attachment', models.FileField(upload_to=b'')),
                ('image', models.ImageField(upload_to=b'')),
                ('url', models.URLField()),
                ('uuid', models.UUIDField()),
                ('gender', models.CharField(max_length=6, choices=[(b'm', b'male'), (b'f', b'female')])),
                ('first_time_application', models.BooleanField()),
            ],
        ),
    ]
