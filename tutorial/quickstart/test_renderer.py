import json
import pytest


@pytest.mark.skipif(True, reason='Code needs refactoring to be testable.')
def test_hydra_renderer():
    from renderers import HydraRenderer
    renderer = HydraRenderer()

    result = json.loads(renderer.render({}))

    assert result.get('@context') == 'http://www.w3.org/ns/hydra/context.jsonld'  # noqa
    assert result.get('@id') == 'http://127.0.0.1:8000/application'
    assert result.get('@type') == 'PagedCollection'


def test_json_schema_renderer_empty():
    from renderers import JSONSchemaRenderer
    renderer = JSONSchemaRenderer()

    result = json.loads(renderer.render({}))

    assert result.get('title') == 'Example Schema'
    assert result.get('type') == 'object'


def test_json_schema_renderer():
    from renderers import JSONSchemaRenderer
    renderer = JSONSchemaRenderer()

    result = json.loads(
        renderer.render(
            {
                'username': u'johndoe',
                'email': u'john@doe.com',
                'groups': []
            }
        )
    )

    assert result.get('type') == 'object'
    assert result.get('properties').keys() == \
        [u'username', u'age', u'email']
    assert result.get('properties').get('username').get('type') == \
        u'string'
    assert result.get('properties').get('email').get('type') == \
        u'string'
    assert result.get('properties').get('age').get('type') == \
        u'integer'
