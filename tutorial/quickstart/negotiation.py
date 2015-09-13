from rest_framework.negotiation import BaseContentNegotiation
from tutorial.quickstart.renderers import JSONSchemaRenderer
from tutorial.quickstart.renderers import HydraRenderer


class IgnoreClientContentNegotiation(BaseContentNegotiation):

    def select_parser(self, request, parsers):
        """
        Select the first parser in the `.parser_classes` list.
        """
        return parsers[0]

    def select_renderer(self, request, renderers, format_suffix):
        """
        Select the first renderer in the `.renderer_classes` list.
        """
        if 'application/json' in request.content_type or \
           request.query_params.get('format') == 'json':
            for renderer in renderers:
                if isinstance(renderer, HydraRenderer):
                    return (renderer, renderer.media_type)
        elif 'application/schema+json' in request.content_type or \
             request.query_params.get('format') == 'schema_json':
            for renderer in renderers:
                if isinstance(renderer, JSONSchemaRenderer):
                    return (renderer, renderer.media_type)
        return (renderers[0], renderers[0].media_type)
