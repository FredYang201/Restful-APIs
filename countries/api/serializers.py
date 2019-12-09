from .models import Country
from rest_framework.serializers import ModelSerializer


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = [
            'id',
            'name',
            'capital',
            'population',
            'area',
            'continent',
            'flag',
            'phone',
            'currency']
