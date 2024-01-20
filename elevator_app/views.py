from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Elevator, Request
from .serializers import ElevatorSerializer, RequestSerializer

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=True, methods=['post'])
    def move_up(self, request, pk=None):
        elevator = self.get_object()
        elevator.move_up()
        return Response({'status': 'moving up'})

    @action(detail=True, methods=['post'])
    def move_down(self, request, pk=None):
        elevator = self.get_object()
        elevator.move_down()
        return Response({'status': 'moving down'})

    @action(detail=True, methods=['post'])
    def stop(self, request, pk=None):
        elevator = self.get_object()
        elevator.stop()
        return Response({'status': 'stopped'})


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

