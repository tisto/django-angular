from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from tutorial.quickstart.models import Application
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = (
            'url',
            'username',
            'email',
            'groups',
        )


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.ReadOnlyField()

    class Meta:
        model = Application
