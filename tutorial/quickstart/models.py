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
    firstname = models.CharField(u'First name', max_length=255)
    lastname = models.CharField(u'Last name', max_length=255)
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
    date = models.DateField(u'Date', null=True, blank=True)
    attachment = models.FileField(u'Attachment', null=True, blank=True)
    image = models.ImageField(u'Image', null=True, blank=True)
    url = models.URLField(u'URL', null=True, blank=True)
    uuid = models.UUIDField(u'UUID', null=True, blank=True)
    gender = models.CharField(
        u'Gender',
        max_length=6,
        null=True,
        blank=True,
        choices=(('m', 'male'), ('f', 'female'),)
    )
    first_time_application = models.NullBooleanField(u'First time application')
