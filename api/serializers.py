from django.contrib.auth.models import User, Group
from api.models import Connection, Position, Event, Monitoring
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        fields = ('unitId', 'port', 'value', 'dateTime')

class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ('unitId', 'rDx', 'rDy', 'speed', 'course', 'numSattellites', 'hdop', 'quality', 'dateTime')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('port', 'value', 'unitId', 'dateTime')

class MonitoringSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monitoring
        fields = ('beginTime', 'endTime', 'unitId', 'type', 'min', 'max', 'sum')
