from .models import Movies
from rest_framework.serializers import ModelSerializer


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movies
        fields = ('id', 'movieId', 'name', 'year', 'rate', 'link')