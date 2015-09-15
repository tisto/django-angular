from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from tutorial.quickstart.models import Application
from rest_framework import serializers
from rest_framework import fields
from collections import OrderedDict


# Mapping from Django REST Framework models to JSON schema
# http://www.django-rest-framework.org/api-guide/fields/
# http://json-schema.org/latest/json-schema-core.html#anchor8
REST_MODEL_TO_JSON_SCHEMA_MAPPING = {
    # Boolean Fields
    fields.BooleanField: {'type': 'boolean'},
    fields.NullBooleanField: {'type': 'boolean'},
    # String Fields
    fields.CharField: {'type': 'string'},
    fields.EmailField: {
        'type': 'string',
        'pattern': '^\\S+@\\S+$',
        'description': 'Email address.',
    },
    fields.RegexField: {'type': 'string'},
    fields.SlugField: {'type': 'string'},
    fields.URLField: {'type': 'string'},
    fields.UUIDField: {'type': 'string'},
    fields.FilePathField: {'type': 'string'},
    fields.IPAddressField: {'type': 'string'},
    # Numeric Fields
    fields.IntegerField: {'type': 'integer'},
    fields.FloatField: {'type': 'number'},
    fields.DecimalField: {'type': 'number'},
    # Date and time fields
    fields.DateTimeField: {'type': 'string'},
    fields.DateField: {'type': 'string'},
    fields.TimeField: {'type': 'string'},
    # Choice selection fields
    fields.ChoiceField: {'type': 'string'},
    fields.MultipleChoiceField: {'type': 'string'},
    # File upload fields
    fields.FileField: {'type': 'string'},
    fields.ImageField: {'type': 'string'},
    # Composite fields
    fields.ListField: {'type': 'array'},
    fields.DictField: {'type': 'object'},
    # Miscellaneous fields
    fields.ReadOnlyField: {'type': 'string'},
    fields.HiddenField: {'type': 'string'},
    fields.ModelField: {'type': 'string'},
    fields.SerializerMethodField: {'type': 'string'},
}


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = (
            'url',
            'username',
            'email',
            'groups',
        )


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.ReadOnlyField()

    class Meta:
        model = Application


class JsonSchemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application

    def get_fields(self, *args, **kwargs):
        fields = super(JsonSchemaSerializer, self).get_fields(*args, **kwargs)
        return fields

    def to_representation(self, obj):
        result = {
            "title": self.Meta.model.__doc__,
            "type": "object",
            "properties": OrderedDict()
        }
        for key, value in self.get_fields().items():
            for m_key, m_value in REST_MODEL_TO_JSON_SCHEMA_MAPPING.items():
                if isinstance(value, m_key):
                    mapping_dict = m_value
            result['properties'][key] = {
                'key': key,
                'title': value.label or key
            }
            for m_key, m_value in mapping_dict.items():
                result['properties'][key][m_key] = m_value
        return result
