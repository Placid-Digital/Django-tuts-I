from rest_framework import serializers
from .models import Users, Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


