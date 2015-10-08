# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0014_application_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='first_time_application_reason',
            field=models.CharField(max_length=255, verbose_name='Reason for first time application', null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='age',
            field=models.IntegerField(help_text='Your age', null=True, verbose_name='Age', blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='attachment',
            field=models.FileField(help_text='File attachment', upload_to='', verbose_name='Attachment', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(help_text='Gender help text', null=True, max_length=6, verbose_name='Gender', choices=[('m', 'male'), ('f', 'female')], blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='image',
            field=models.ImageField(help_text='Image attachment', upload_to='', verbose_name='Image', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='salutation',
            field=models.CharField(null=True, max_length=255, verbose_name='Salutation', choices=[('mr', 'Mr'), ('mrs', 'Mrs'), ('ms', 'Ms')], blank=True),
        ),
    ]
