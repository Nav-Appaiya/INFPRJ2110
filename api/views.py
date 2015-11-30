# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from api.models import Snippet
from rest_framework import request

@api_view(['GET'])
@permission_classes([  ]) # Beveiliging hier later met [IsAdminUser]
def city_gis(request, format=None):
    """
    Available endpoints:
    `Connection`,
    `Event`,
    `Monitoring`,
    `Position`
    """

    return Response(
        {
            'connections': request.build_absolute_uri('connections'),
            'events': request.build_absolute_uri('events'),
            'monitoring': request.build_absolute_uri('monitoring'),
            'positions': request.build_absolute_uri('positions'),
        }
    )

@api_view(['GET'])
@permission_classes([  ]) # Beveiliging hier later met [IsAdminUser]
def connections(request, format=None):
    """
    Connections
    """
    con = dict(connection={
        "port": "Connection",
        "value": 0,
        "dateTime": {
            "date": {
                "year": 2015,
                "month": 3,
                "day": 15
            },
            "time": {
                "hour": 14,
                "minute": 11,
                "second": 1,
                "nano": 0
            }
        },
        "unitId": 999
    })

    return Response(con)