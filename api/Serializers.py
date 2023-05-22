from events.models import *
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

# class EventSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         fieldds = ['title','category']