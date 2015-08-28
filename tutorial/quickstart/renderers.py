from rest_framework import renderers
import json


class HydraRenderer(renderers.BaseRenderer):
    media_type = 'application/json'
    format = 'json'

    def render(self, data, media_type=None, renderer_context=None):
        return json.dumps({
            '@context': 'http://www.w3.org/ns/hydra/context.jsonld',
            '@id': '',
            '@type': 'PagedCollection',
            'totalItems': data['count'],
            'itemsPerPage': '10',
            'firstPage': '',
            'nextPage': data['next'],
            'previousPage': data['previous'],
            'lastPage': '',
            'member': data['results'],
            'operation': [
                {
                    '@type': 'CreateResourceOperation',
                    'method': 'POST',
                    'title': 'Creates a new user',
                    'expects': '',
                    'returns': ''
                },
                {
                    '@type': 'ReplaceResourceOperation',
                    'method': 'PUT',
                    'title': 'Updates an existing user'
                },
                {
                    '@type': 'DeleteResourceOperation',
                    'method': 'DELETE',
                    'title': 'Removes an existing user'
                },
            ]
        })
