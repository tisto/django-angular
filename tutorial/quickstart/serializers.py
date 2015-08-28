from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    operation = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'url',
            'username',
            'email',
            'groups',
            'operation'
        )

    def get_operation(self, obj):
        return [
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


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
