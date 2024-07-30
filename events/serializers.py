from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    end_time = serializers.SerializerMethodField()
    time_until_event = serializers.SerializerMethodField()
    formatted_event = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'name', 'start_time', 'duration', 'timezone', 'end_time', 'time_until_event', 'formatted_event']

    def get_end_time(self, obj):
        return obj.get_end_time()

    def get_time_until_event(self, obj):
        return obj.time_until_event()

    def get_formatted_event(self, obj):
        return obj.format_event()

class TimezoneSerializer(serializers.Serializer):
    timezone = serializers.CharField(max_length=63)
