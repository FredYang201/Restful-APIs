from rest_framework.serializers import ModelSerializer
from .models import Player


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['id','name', 'team', 'number', 'link', 'position', 'height', 'weight', 'born', 'age', 'years_in_nba']