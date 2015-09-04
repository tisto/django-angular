from django.db import models


class Application(models.Model):

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    attachment = models.FileField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    uuid = models.UUIDField(null=True, blank=True)
    gender = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        choices=(('m', 'male'), ('f', 'female'),)
    )
    first_time_application = models.NullBooleanField()
