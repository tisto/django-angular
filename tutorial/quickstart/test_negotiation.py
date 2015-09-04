import json


def test_content_negotiation_application_json(admin_client):
    response = admin_client.get(
        '/application/',
        HTTP_CONTENT_TYPE='application/json'
    )
    assert 200 == response.status_code
    assert 'application/json' in response.get('Content-Type')
    assert json.loads(response.content)


def test_content_negotiation_json_schema(admin_client):
    response = admin_client.get(
        '/application/',
        HTTP_CONTENT_TYPE='application/schema+json'
    )
    assert 200 == response.status_code
    assert 'application/schema+json' in response.get('Content-Type')
    assert json.loads(response.content)
#    assert json.loads(response.content)\
#        .get('properties').get('firstname') is not None
