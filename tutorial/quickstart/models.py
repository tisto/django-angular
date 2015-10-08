# -*- coding: utf-8 -*-
from django.db import models


class Application(models.Model):

    title = models.CharField(
        u'Title',
        help_text=u'Title of the application',
        max_length=255
    )

    description = models.TextField(
        u'Description',
        help_text=u'Description of the application',
        null=True,
        blank=True
    )

    salutation = models.CharField(
        u'Salutation',
        null=True,
        blank=True,
        max_length=255,
        choices=(
            ('mr', 'Mr'),
            ('mrs', 'Mrs'),
            ('ms', 'Ms'),
        )
    )

    firstname = models.CharField(
        u'First name',
        help_text=u'Your first name',
        max_length=255
    )

    lastname = models.CharField(
        u'Last name',
        help_text=u'Your last name',
        max_length=255
    )

    street = models.CharField(
        u'Street',
        help_text=u'Your street name',
        null=True,
        max_length=255
    )

    house_number = models.CharField(
        u'House number',
        null=True,
        max_length=255
    )

    zip_number = models.CharField(
        u'ZIP number',
        null=True,
        max_length=5
    )

    city = models.CharField(
        u'City',
        null=True,
        max_length=255
    )

    country = models.CharField(
        u'Country',
        null=True,
        max_length=255
    )

    email = models.EmailField(
        u'Email address',
        help_text=u'Your email address',
        null=True,
        blank=True
    )

    age = models.IntegerField(
        u'Age',
        help_text='Your age',
        null=True,
        blank=True
    )

    date = models.DateField(
        u'Date',
        help_text=u'Example of a Django DateField with a date picker',
        auto_now=True,
        null=True
    )

    datetime = models.DateTimeField(
        u'Datetime',
        help_text=u'Example of a Django DateTimeField with a datetime picker',
        auto_now=True,
        null=True
    )

    time = models.TimeField(
        u'Time',
        help_text=u'Example of a Django TimeField with a time picker',
        auto_now=True,
        null=True
    )

    attachment = models.FileField(
        u'Attachment',
        help_text=u'File attachment',
        null=True,
        blank=True
    )

    image = models.ImageField(
        u'Image',
        help_text=u'Image attachment',
        null=True,
        blank=True
    )

    url = models.URLField(
        u'URL',
        help_text=u'URL help text',
        null=True,
        blank=True
    )

    uuid = models.UUIDField(
        u'UUID',
        help_text=u'UUID help text',
        null=True,
        blank=True
    )

    gender = models.CharField(
        u'Gender',
        help_text=u'Gender help text',
        max_length=6,
        null=True,
        blank=True,
        choices=(('m', 'male'), ('f', 'female'),)
    )

    first_time_application = models.NullBooleanField(
        u'First time application',
        help_text=u'Is this your first time application?',
    )

    first_time_application_reason = models.CharField(
        u'Reason for first time application',
        null=True,
        max_length=255
    )
