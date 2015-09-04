from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework import viewsets
from tutorial.quickstart.models import Application
from tutorial.quickstart.serializers import UserSerializer
from tutorial.quickstart.serializers import GroupSerializer
from tutorial.quickstart.serializers import ApplicationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows applications to be viewed or edited.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
