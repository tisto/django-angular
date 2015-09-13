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
    fields.BooleanField: 'boolean',
    fields.NullBooleanField: 'boolean',
    # String Fields
    fields.CharField: 'string',
    fields.EmailField: 'string',
    fields.RegexField: 'string',
    fields.SlugField: 'string',
    fields.URLField: 'string',
    fields.UUIDField: 'string',
    fields.FilePathField: 'string',
    fields.IPAddressField: 'string',
    # Numeric Fields
    fields.IntegerField: 'integer',
    fields.FloatField: 'number',
    fields.DecimalField: 'number',
    # Date and time fields
    fields.DateTimeField: 'string',
    fields.DateField: 'string',
    fields.TimeField: 'string',
    # Choice selection fields
    fields.ChoiceField: 'string',
    fields.MultipleChoiceField: 'string',
    # File upload fields
    fields.FileField: 'string',
    fields.ImageField: 'string',
    # Composite fields
    fields.ListField: 'array',
    fields.DictField: 'object',
    # Miscellaneous fields
    fields.ReadOnlyField: 'string',
    fields.HiddenField: 'string',
    fields.ModelField: 'string',
    fields.SerializerMethodField: 'string',
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
            new_value = 'UNKNOWN'
            for m_key, m_value in REST_MODEL_TO_JSON_SCHEMA_MAPPING.items():
                if isinstance(value, m_key):
                    new_value = m_value
            result['properties'][key] = {
                'key': key,
                'title': value.label or key,
                'type': new_value
            }
        return result
