from rest_framework import serializers
from .models import Surah, Dua

class SurahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surah
        fields = "__all__" 

class DuaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dua
        fields = "__all__"

