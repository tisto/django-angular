import json
import pytest
from tutorial.quickstart.models import Application


@pytest.mark.django_db()
def test_application_json_list_view(admin_client):
    app = Application()
    app.title = u'My first application'
    app.firstname = u'John'
    app.lastname = u'Doe'
    app.email = u'john@doe.com'
    app.save()

    response = admin_client.get(
        '/application/',
        HTTP_ACCEPT='application/json'
    )

    assert 200 == response.status_code
    assert 'application/json' in response.get('Content-Type')
    assert u'PagedCollection' == json.loads(
        response.content.decode()).get('@type')
    assert 1 == len(json.loads(response.content.decode()).get('member'), )
    assert u'My first application' == \
        json.loads(response.content.decode()).get('member')[0].get('title')


@pytest.mark.django_db()
def test_application_json_detail_view(admin_client):
    app = Application()
    app.title = u'My first application'
    app.firstname = u'John'
    app.lastname = u'Doe'
    app.email = u'john@doe.com'
    app.save()

    response = admin_client.get(
        '/application/{}/'.format(app.id),
        HTTP_ACCEPT='application/json'
    )

    assert 200 == response.status_code
    assert 'application/json' in response.get('Content-Type')
    assert u'Resource' == json.loads(response.content.decode()).get('@type')
    assert u'My first application' == \
        json.loads(response.content.decode()).get('title')
    assert 'parent' in json.loads(response.content.decode()).keys()
    assert u'http://testserver/application/' == \
        json.loads(response.content.decode()).get('parent')
