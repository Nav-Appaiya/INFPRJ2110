# -*- coding: utf-8 -*-
"""
api.users.views
~~~~~~~~~~~~~~~

This module implements the logic for user views.

"""
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from api.serializers import PositionSerializer, EventSerializer, MonitoringSerializer
from .permissions import IsAdminOrSelf
from .serializers import UserSerializer, PasswordSerializer, GroupSerializer, ConnectionSerializer
from api.models import Connection, Position, Event, Monitoring

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    To set a password, POST a `password` on the `/set_password/` url.

    To set a unusuable password, set `!` as a password.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrSelf,)

    @detail_route(methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.DATA)
        if serializer.is_valid():
            password = self.request.DATA['password']
            if password == '!':
                user.set_unusable_password()
            else:
                user.set_password(password)
                user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a single or list of groups.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAdminUser,)

class ConnectionViewSet(viewsets.ModelViewSet):
    """
    Endpoint for retrieving connections data for CityGis
    """
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    permission_classes = (IsAdminUser,)

class PositionViewSet(viewsets.ModelViewSet):
    """
    Endpoint for retrieving Position data for CityGis
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = (IsAdminUser,)

class EventViewSet(viewsets.ModelViewSet):
    """
    Endpoint for retrieving Event data for CityGis
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAdminUser,)

class MonitoringViewSet(viewsets.ModelViewSet):
    """
    Endpoint for retrieving Monitoring data for CityGis
    """
    queryset = Monitoring.objects.all()
    serializer_class = MonitoringSerializer
    permission_classes = (IsAdminUser,)