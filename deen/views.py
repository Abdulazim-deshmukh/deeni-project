from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Surah, Dua
from .serializers import SurahSerializer, DuaSerializer

class SurahViewSet(ReadOnlyModelViewSet):
    queryset = Surah.objects.all()
    serializer_class = SurahSerializer


class DuaViewSet(ReadOnlyModelViewSet):
    queryset = Dua.objects.all()
    serializer_class = DuaSerializer
