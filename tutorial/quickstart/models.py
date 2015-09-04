from django.db import models


class Application(models.Model):

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField(null=True)
    description = models.TextField()
    date = models.DateField(null=True)
    attachment = models.FileField()
    image = models.ImageField()
    url = models.URLField()
    uuid = models.UUIDField(null=True)
    gender = models.CharField(
        max_length=6,
        choices=(('m', 'male'), ('f', 'female'),)
    )
    first_time_application = models.NullBooleanField()
