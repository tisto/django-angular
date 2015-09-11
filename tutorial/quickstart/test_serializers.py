from django.contrib.auth.models import User
from serializers import JsonSchemaSerializer
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
    from serializers import UserSerializer
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
    assert {'type': 'string'} == result.get('properties').get('firstname')
    assert {'type': 'string'} == result.get('properties').get('lastname')
    assert {'type': 'string'} == result.get('properties').get('email')
    assert {'type': 'boolean'} == result.get('properties').get('first_time_application')  # noqa
