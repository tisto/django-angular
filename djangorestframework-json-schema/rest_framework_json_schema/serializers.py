# -*- coding: utf-8 -*-
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
        'validationMessage': 'Please enter a valid email address.'
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
    fields.DateTimeField: {'type': 'string', 'format': 'datetimepicker'},
    fields.DateField: {'type': 'string', 'format': 'datepicker'},
    fields.TimeField: {'type': 'string', 'format': 'timepicker'},
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


class JsonSchemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application

    def get_fields(self, *args, **kwargs):
        fields = super(JsonSchemaSerializer, self).get_fields(*args, **kwargs)
        return fields

    def to_representation(self, obj):
        result = {
            'title': self.Meta.model.__doc__,
            'type': 'object',
            'form': [],
            'required': [],
            'properties': OrderedDict()
        }
        # Schema
        for key, value in self.get_fields().items():
            mapping_dict = REST_MODEL_TO_JSON_SCHEMA_MAPPING[type(value)]
            result['properties'][key] = {
                'key': key,
                'title': value.label or key,
                'description': value.help_text or '',
            }
            for m_key, m_value in mapping_dict.items():
                result['properties'][key][m_key] = m_value

        # Required
        for key, value in self.get_fields().items():
            if value.required:
                result['required'].append(key)
        # Form Helper
        result['form'].append({
            'type': 'help',
            'helpvalue': '<div class="alert alert-info">Example Form</div>'
        })

        # Form Keys
        for key, value in self.get_fields().items():
            result['form'].append(key)

        # Form Actions
        result['form'].append(
            {
                'type': 'submit',
                'title': 'Save'
            }
        )
        result['form'].append(
            {
                'type': 'button',
                'title': 'Cancel',
                'style': 'btn-default',
                'onClick': 'clearForm(form)'
            }
        )
        return result
