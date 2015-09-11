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
