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
            'totalItems': data.get('count'),
            'itemsPerPage': '10',
            'firstPage': '',
            'nextPage': data.get('next'),
            'previousPage': data.get('previous'),
            'lastPage': '',
            'member': data.get('results'),
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


class JSONSchemaRenderer(renderers.JSONRenderer):
    media_type = 'application/schema+json'
    format = 'json'

    def render(self, data, media_type=None, renderer_context=None):
        return json.dumps({
            "title": "Example Schema",
            "type": "object",
            "properties": {
                "username": {
                    "title": "Username",
                    "type": "string"
                },
                "email": {
                    "title": "Email",
                    "type": "string"
                },
                "age": {
                    "title": "Age",
                    "description": "Age in years",
                    "type": "integer",
                    "minimum": 0
                }
            },
            "required": ["username", "email"]
        })
