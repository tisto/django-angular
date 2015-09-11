from tutorial.quickstart.models import Application
import json
import pytest


@pytest.mark.django_db()
def test_application_schema_json_detail_view(admin_client):
    app = Application()
    app.title = u'My first application'
    app.firstname = u'John'
    app.lastname = u'Doe'
    app.email = u'john@doe.com'
    app.save()

    response = admin_client.get(
        '/application/{}/'.format(app.id),
        HTTP_CONTENT_TYPE='application/schema+json'
    )

    assert 200 == response.status_code
    assert 'application/schema+json' in response.get('Content-Type')
    assert 'title' in json.loads(response.content).get('properties')
