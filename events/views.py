from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
import pytz

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TimezoneListView(APIView):
    def get(self, request):
        timezones = pytz.all_timezones
        return Response(timezones)