# -*- coding: utf-8 -*-
from rest_framework import renderers
from rest_framework.reverse import reverse
from .serializers import JsonSchemaSerializer

from collections import OrderedDict

from rest_framework import renderers

import json


class JSONSchemaRenderer(renderers.JSONRenderer):
    media_type = 'application/schema+json'
    format = 'schema+json'
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        serializer = JsonSchemaSerializer()
        result = serializer.to_representation(data)
        return json.dumps(result)
