from email.policy import default
from django.db import models

# Create your models here.

class Artise(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    age = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.first_name

class Song(models.Model):
    artise_id= models.ForeignKey(Artise, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_released = models.DateField(max_length=50)
    likes = models.TextField(blank=True, null=True)

    def __str__(self):
       return self.title
    
class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, default=True)
    content = models.TextField(max_length = 8000)

    def __str__(self):
       return self.content   
