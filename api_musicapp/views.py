from rest_framework.decorators import api_view
from rest_framework.response import Response

from musicapp.models import *
from musicapp.serializers import *

# Create your views here.

@api_view(['GET', 'POST'])
def artise_home(request, *args, **kwargs):
    serializer = ArtiseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({"invalid": "not a good data"}, status=400)

@api_view(['GET', 'POST'])
def song_home(request, *args, **kwargs):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({"invalid": "not a good data"}, status=400)

@api_view(['GET', 'POST'])
def lyric_home(request, *args, **kwargs):
    serializer = LyricSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({"invalid": "not a good data"}, status=400)     
    