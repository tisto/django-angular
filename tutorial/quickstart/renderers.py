from rest_framework import renderers
from rest_framework.reverse import reverse
import json


class HydraRenderer(renderers.BaseRenderer):

    media_type = 'application/json'
    format = 'json'

    def render(self, data, media_type=None, renderer_context=None):
        request = renderer_context.get('request')
        result = {
            '@context': 'http://www.w3.org/ns/hydra/context.jsonld'
        }
        if renderer_context.get('kwargs').get('pk'):
            result['@type'] = u'Resource'
            result['@id'] = reverse(
                'application-detail',
                args=[renderer_context.get('kwargs').get('pk')],
                request=request
            )
            result['parent'] = reverse(
                'application-list',
                request=request
            )
            for key, value in data.items():
                result[key] = value
        else:
            result['@type'] = u'PagedCollection'
            result['@id'] = reverse(
                'application-list',
                request=request
            )
            result['member'] = [
                {
                    '@id': reverse(
                        'application-detail',
                        args=[x.get('id')],
                        request=request
                    ),
                    'title': x.get('title')
                }
                for x in data
            ]
            result['operation'] = [
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
            result['totalItems'] = None
            result['itemsPerPage'] = '10'
            result['firstPage'] = None
            result['nextPage'] = None
            result['previousPage'] = None
            result['lastPage'] = None
        return json.dumps(result)


class JSONSchemaRenderer(renderers.JSONRenderer):
    media_type = 'application/schema+json'
    format = 'schema+json'

    def render(self, data, media_type=None, renderer_context=None):
        from serializers import JsonSchemaSerializer
        serializer = JsonSchemaSerializer()
        result = serializer.to_representation(data)
        return json.dumps(result)
