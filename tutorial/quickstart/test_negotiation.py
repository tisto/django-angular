import json


def test_content_negotiation_application_json(admin_client):
    response = admin_client.get(
        '/application/',
        HTTP_ACCEPT='application/json'
    )
    assert 200 == response.status_code
    assert 'application/json' in response.get('Content-Type')
    assert json.loads(response.content)
    assert json.loads(response.content).get('@context')
    assert json.loads(response.content).get('@id')


def test_content_negotiation_application_json_url(admin_client):
    response = admin_client.get(
        '/application/?format=json',
    )
    assert 200 == response.status_code
    assert 'application/json' in response.get('Content-Type')
    assert json.loads(response.content)
    assert json.loads(response.content).get('@context')
    assert json.loads(response.content).get('@id')


def test_content_negotiation_json_schema(admin_client):
    response = admin_client.get(
        '/application/',
        HTTP_ACCEPT='application/schema+json'
    )
    assert 200 == response.status_code
    assert 'application/schema+json' in response.get('Content-Type')
    assert json.loads(response.content)
    assert json.loads(response.content).get('type') == u'object'
    assert json.loads(response.content).get('properties')


def test_content_negotiation_json_schema_url(admin_client):
    response = admin_client.get(
        '/application/?format=json_schema',
    )
    assert 200 == response.status_code
    assert 'application/schema+json' in response.get('Content-Type')
    assert json.loads(response.content)
    assert json.loads(response.content).get('type') == u'object'
    assert json.loads(response.content).get('properties')
