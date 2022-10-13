from urllib import request
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from musicapp.models import Artise, Song, Lyric
from musicapp.serializers import ArtiseSerializer, SongSerializer, LyricSerializer
from rest_framework import status
from rest_framework import generics

# Create your views here.

class ArtiseDetailAPIView(generics.RetrieveAPIView):
    queryset = Artise.objects.all()
    serializer_class = ArtiseSerializer

artise_detail_view = ArtiseDetailAPIView.as_view()

class SongDetailAPIView(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

song_detail_view = SongDetailAPIView.as_view()

class LyricDetailAPIView(generics.RetrieveAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer

lyric_detail_view =LyricDetailAPIView.as_view()

class ArtiseCreate(APIView):
    serializer = ArtiseSerializer()
    def get_object(self, serializer):
        try:
            return Artise.objects.get(serializer=serializer)
        except Artise.DoesNotExist:
            raise Http404

    def get(self, serializer):
        artise = self.get_object(serializer)
        return Response(serializer.data)

    def create(self, serializer):
        first_name = serializer.get('first_name')
        last_name = serializer.get('last_name')
        age = serializer.get('age')
        if first_name is None:
            first_name = first_name
        serializer.save(first_name=first_name)

        if last_name is None:
            last_name = last_name
        serializer.save(last_name=last_name)

        if age is None:
            age = age
        serializer.save(age=age)
        ArtiseCreate.get(serializer)    

# class SongList(APIView):
#     def get(self, request, format=None):
#         music = Song.objects.all()
#         serializer = SongSerializer(music, many=True)
#         return Response(serializer.data)

# class LyricList(APIView):
#     def get(self, request, format=None):
#         music = Lyric.objects.all()
#         serializer = LyricSerializer(music, many=True)
      

class ArtiseList(APIView):
    def get(self, request, format=None):
        music = Artise.objects.all()
        serializer = ArtiseSerializer(music, many=True)
        return Response(serializer.data)

class SongList(APIView):
    def get(self, request, format=None):
        music = Song.objects.all()
        serializer = SongSerializer(music, many=True)
        return Response(serializer.data)

class LyricList(APIView):
    def get(self, request, format=None):
        music = Lyric.objects.all()
        serializer = LyricSerializer(music, many=True)
        return Response(serializer.data)        

class ArtiseUpdate(APIView):
    def get_object(self, pk):
        try:
            return Artise.objects.get(pk=pk)
        except Artise.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        artise = self.get_object(pk)
        serializer = ArtiseSerializer(artise)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        artise = self.get_object(pk)
        serializer = ArtiseSerializer(artise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class ArtiseDelete(APIView):
    def get_object(self, pk):
        try:
            return Artise.objects.get(pk=pk)
        except Artise.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        artise = self.get_object(pk)
        serializer = ArtiseSerializer(artise)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        artise = self.get_object(pk)
        artise.delete()

class SongUpdate(APIView):
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)       

class SongDelete(APIView):
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        song = self.get_object(pk)
        song.delete()      

class LyricUpdate(APIView):
    def get_object(self, pk):
        try:
            return Lyric.objects.get(pk=pk)
        except Lyric.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        lyric = self.get_object(pk)
        serializer = LyricSerializer(lyric)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        lyric = self.get_object(pk)
        serializer = LyricSerializer(lyric, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)       

class LyricDelete(APIView):
    def get_object(self, pk):
        try:
            return Lyric.objects.get(pk=pk)
        except Lyric.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        lyric = self.get_object(pk)
        serializer = LyricSerializer(lyric)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        lyric = self.get_object(pk)
        lyric.delete()                                             

@api_view(['GET', 'POST'])
def song_all_view(request,pk):
    if request.method == "GET":
        if Song.objects.filter(pk = pk).exists():
            Song = Song.objects.get(pk = pk)
            data = SongSerializer(Song, many=False)
            return Response(data.data)
    if request.method == "POST":
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save() 
            return Response(serializer.data)

def lyric_all_view(request,pk):
    if request.method == 'GET':
        if Lyric.object.fliter(pk = pk).exist():
            Lyric = Lyric.object.get(pk = pk)
            data = LyricSerializer(Lyric, many=False)
            return Response(data.data)
    if request.method == "POST":
        serializer = LyricSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save() 
            return Response(serializer.data) 
                   