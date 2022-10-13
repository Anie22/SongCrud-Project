from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('artise/<int:pk>/', views.artise_detail_view), 
    path('', views.ArtiseList.as_view()),
    path('artise/create', views.ArtiseCreate.as_view()),
    path('artise/<int:pk>/update', views.ArtiseUpdate.as_view()),
    path('artise/<int:pk>/delete', views.ArtiseDelete.as_view()),
    path('<int:pk>/', views.song_detail_view),
    path('song/', views.SongList.as_view()),
    path('song/<int:pk>/update', views.SongUpdate.as_view()),
    path('song/<int:pk>/delete', views.SongDelete.as_view()),
    path('lyric/<int:pk>/', views.lyric_detail_view),
    path('lyric/', views.LyricList.as_view()),
    path('lyric/<int:pk>/update', views.LyricUpdate.as_view()),
    path('lyric/<int:pk>/delete', views.LyricDelete.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)