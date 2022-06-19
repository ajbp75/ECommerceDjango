from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedatas


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedatas
    serializer_class = MovieSerializer
