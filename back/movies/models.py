from django.db import models
from django.conf import settings


class Genre(models.Model):
    id = models.IntegerField(primary_key=True) # 장르 ID
    name = models.CharField(max_length=50)


class Actor(models.Model):
    id = models.IntegerField(primary_key=True) # 배우 ID
    name = models.CharField(max_length=100)
    profile_path = models.TextField(null=True, blank=True)


class Movie(models.Model):
    id = models.IntegerField(primary_key=True) # 영화 ID
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True, blank=True) # 내용
    popularity = models.FloatField(null=True, blank=True) # 인기도
    poster_path = models.TextField(null=True, blank=True) # 포스터 주소
    release_date = models.DateTimeField(null=True, blank=True) # 개봉일
    vote_average = models.FloatField(null=True, blank=True) # 평점
    vote_count = models.IntegerField(null=True, blank=True) # 평점 투표 수
    # runtime = models.Field() # 상영 시간
    genres = models.ManyToManyField(Genre) # 해당 영화의 장르
    actors = models.ManyToManyField(Actor) # 해당 영화의 배우


class Character(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='actor_character')
    character = models.CharField(max_length=100)

class Director(models.Model):
    id = models.IntegerField(primary_key=True) 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_path = models.TextField(null=True, blank=True)


class Rank(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.FloatField()




    

