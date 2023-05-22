from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from events.models import Event
from .Serializers import EventSerializer

@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response( serializer.data , status=status.HTTP_200_OK )