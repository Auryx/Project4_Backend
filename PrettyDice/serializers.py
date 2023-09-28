from .models import Dice
from rest_framework import serializers

class DiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model to serialize
        model = Dice
        # fields to show in json
        fields = ('id', 'name', 'cost', 'link', 'description')