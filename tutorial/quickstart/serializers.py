from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from tutorial.quickstart.models import Application
from rest_framework import serializers
from rest_framework import fields

# http://json-schema.org/latest/json-schema-core.html#anchor8
REST_MODEL_TO_JSON_SCHEMA_MAPPING = {
    #models.CharField: 'array',
    fields.BooleanField: 'boolean',
    fields.NullBooleanField: 'boolean',
    #models.IntegerField: 'integer',
    #models.DecimalField: 'number',
    #models.FloatField: 'number',
    # 'null',
    # 'object',
    fields.IntegerField: 'integer',
    fields.CharField: 'string',
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
            "properties": {
                "firstname": {
                    "type": "string"
                },
                "lastname": {
                    "type": "string"
                },
                "email": {
                    "type": "string"
                }
            }
        }
        for key, value in self.get_fields().items():
            new_value = 'UNKNOWN'
            for m_key, m_value in REST_MODEL_TO_JSON_SCHEMA_MAPPING.items():  # noqa
                if isinstance(value, m_key):
                    new_value = m_value
            result['properties'][key] = {'type': new_value}
        return result

    def to_internal_value(self, data):
        import pdb; pdb.set_trace()

