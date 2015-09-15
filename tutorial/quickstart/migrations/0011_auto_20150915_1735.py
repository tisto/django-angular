# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0010_auto_20150904_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='datetime',
            field=models.DateTimeField(auto_now=True, verbose_name='Datetime', null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='time',
            field=models.TimeField(auto_now=True, verbose_name='Time', null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='age',
            field=models.IntegerField(help_text=b'Your age', null=True, verbose_name='Age', blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='attachment',
            field=models.FileField(upload_to=b'', null=True, verbose_name='Attachment', blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date', null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='description',
            field=models.TextField(help_text='Description of the application', null=True, verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(help_text='Your email address', max_length=254, null=True, verbose_name='Email address', blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='first_time_application',
            field=models.NullBooleanField(verbose_name='First time application'),
        ),
        migrations.AlterField(
            model_name='application',
            name='firstname',
            field=models.CharField(max_length=255, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Gender', choices=[(b'm', b'male'), (b'f', b'female')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='image',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='Image', blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='lastname',
            field=models.CharField(max_length=255, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='application',
            name='title',
            field=models.CharField(help_text='Title of the application', max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='application',
            name='url',
            field=models.URLField(null=True, verbose_name='URL', blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='uuid',
            field=models.UUIDField(null=True, verbose_name='UUID', blank=True),
        ),
    ]
