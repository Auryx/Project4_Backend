from .models import Dice
from rest_framework import viewsets, permissions
from .serializers import DiceSerializer

class DiceViewSet(viewsets.ModelViewSet):
    # queryset: list of all x objects
    queryset = Dice.objects.all()
    # serializer_class: control which serializer should be used
    serializer_class = DiceSerializer
    # permissions: API access control
    permission_classes = [permissions.AllowAny]