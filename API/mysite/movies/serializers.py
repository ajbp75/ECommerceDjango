from rest_framework import serializers
from .models import Moviedatas


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moviedatas
        fields = ['id', 'name', 'duration', 'rating']
