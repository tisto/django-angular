# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework_json_schema.serializers import JsonSchemaSerializer
from tutorial.quickstart.serializers import UserSerializer
from tutorial.quickstart.models import Application

import pytest


@pytest.fixture
def django_users():
    User.objects.create_user('john-doe', 'john.doe@example.com', 'secret')
    User.objects.create_user('jane-doe', 'jane.doe@example.com', 'secret')
    User.objects.create_user('joey-doe', 'joey.doe@example.com', 'secret')


@pytest.mark.django_db
def test_admin_user(admin_user):
    me = User.objects.get(username='admin')
    assert me.is_superuser


@pytest.mark.django_db
def test_users(django_users):
    users = User.objects.all()
    assert [u'john-doe', u'jane-doe', u'joey-doe'] == [x.username for x in users]  # noqa


def test_user_serializer():
    serializer = UserSerializer()

    assert ('url', 'username', 'email', 'groups') == \
        tuple(serializer.fields.keys())


@pytest.mark.django_db
def test_json_schema_serializer():
    app = Application()
    app.title = u'My first application'
    app.firstname = u'John'
    app.lastname = u'Doe'
    app.email = u'john@doe.com'
    app.save()

    serializer = JsonSchemaSerializer()
    result = serializer.to_representation(app)

    assert result.get('title').startswith('Application')
    assert 'object' == result.get('type')

    assert 'salutation' == result['properties']['salutation']['key']
    assert 'salutation' == result['properties']['salutation']['title']
    assert 'string' == result['properties']['salutation']['type']
    assert 'salutation' in result['form']

    assert 'firstname' == result['properties']['firstname']['key']
    assert 'First name' == result['properties']['firstname']['title']
    assert 'string' == result['properties']['firstname']['type']
    assert 'firstname' in result['required']
    assert 'firstname' in result['form']

    assert 'lastname' == result['properties']['lastname']['key']
    assert 'Last name' == result['properties']['lastname']['title']
    assert 'string' == result['properties']['lastname']['type']
    assert 'lastname' in result['form']

    assert 'email' == result['properties']['email']['key']
    assert 'Email address' == result['properties']['email']['title']
    assert 'string' == result['properties']['email']['type']
    assert '^\\S+@\\S+$' == result['properties']['email']['pattern']
    assert 'email' in result['form']

    assert 'first_time_application' == result['properties']['first_time_application']['key']  # noqa
    assert 'first_time_application' == result['properties']['first_time_application']['title']  # noqa
    assert 'boolean' == result['properties']['first_time_application']['type']
    assert 'first_time_application' in result['form']
