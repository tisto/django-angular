# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0011_auto_20150915_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='city',
            field=models.CharField(max_length=255, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='application',
            name='house_number',
            field=models.CharField(max_length=255, null=True, verbose_name='House number'),
        ),
        migrations.AddField(
            model_name='application',
            name='street',
            field=models.CharField(help_text='Your street name', max_length=255, null=True, verbose_name='Street'),
        ),
        migrations.AddField(
            model_name='application',
            name='zip_number',
            field=models.CharField(max_length=255, null=True, verbose_name='ZIP number'),
        ),
        migrations.AlterField(
            model_name='application',
            name='attachment',
            field=models.FileField(help_text='File attachment', upload_to=b'', null=True, verbose_name='Attachment', blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='date',
            field=models.DateField(auto_now=True, help_text='Example of a Django DateField with a date picker', null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='application',
            name='datetime',
            field=models.DateTimeField(auto_now=True, help_text='Example of a Django DateTimeField with a datetime picker', null=True, verbose_name='Datetime'),
        ),
        migrations.AlterField(
            model_name='application',
            name='first_time_application',
            field=models.NullBooleanField(help_text='Is this your first time application?', verbose_name='First time application'),
        ),
        migrations.AlterField(
            model_name='application',
            name='firstname',
            field=models.CharField(help_text='Your first name', max_length=255, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(choices=[(b'm', b'male'), (b'f', b'female')], max_length=6, blank=True, help_text='Gender help text', null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='application',
            name='image',
            field=models.ImageField(help_text='Image attachment', upload_to=b'', null=True, verbose_name='Image', blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='lastname',
            field=models.CharField(help_text='Your last name', max_length=255, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='application',
            name='time',
            field=models.TimeField(auto_now=True, help_text='Example of a Django TimeField with a time picker', null=True, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='application',
            name='url',
            field=models.URLField(help_text='URL help text', null=True, verbose_name='URL', blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='uuid',
            field=models.UUIDField(help_text='UUID help text', null=True, verbose_name='UUID', blank=True),
        ),
    ]
