import json
import pytest
from tutorial.quickstart.models import Application


@pytest.mark.django_db()
def test_application_json_view(admin_client):
    app = Application()
    app.title = u'My first application'
    app.firstname = u'John'
    app.lastname = u'Doe'
    app.email = u'john@doe.com'
    app.save()
    response = admin_client.get(
        '/application/',
        HTTP_CONTENT_TYPE='application/json'
    )
    assert 200 == response.status_code
    assert 'application/json' in response.get('Content-Type')
    assert 1 == len(json.loads(response.content).get('member'))
    assert u'My first application' == \
        json.loads(response.content).get('member')[0].get('title')
