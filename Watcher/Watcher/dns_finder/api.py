from .models import DnsMonitored, DnsTwisted, Alert
from rest_framework import viewsets, permissions
from .serializers import AlertSerializer, DnsMonitoredSerializer, DnsTwistedSerializer


# DnsMonitored Viewset
class DnsMonitoredViewSet(viewsets.ModelViewSet):
    queryset = DnsMonitored.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DnsMonitoredSerializer


# DnsTwisted Viewset
class DnsTwistedViewSet(viewsets.ModelViewSet):
    queryset = DnsTwisted.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DnsTwistedSerializer


# Alert Viewset
class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = AlertSerializer
