from django.urls import path
from . import views

urlpatterns = [
    path('', views.artise_home),
    path('song/', views.song_home),
    path('lyric/', views.lyric_home)
]