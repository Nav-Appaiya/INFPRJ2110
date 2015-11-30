# -*- coding: utf-8 -*-
from rest_framework import routers

from .views import UserViewSet, GroupViewSet, ConnectionViewSet, PositionViewSet, EventViewSet, MonitoringViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

router.register(r'connections', ConnectionViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'events', EventViewSet)
router.register(r'monitoring', MonitoringViewSet)

urlpatterns = router.urls
