from rest_framework import serializers

from .models import *

class ArtiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artise
        fields = [
            'first_name',
            'last_name',
            'age'
        ]

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
            'artise_id',
            'title',
            'date_released',
            'likes'
        ]

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = [
            'song_id',
            'content'
        ]