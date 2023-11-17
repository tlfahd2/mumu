from django.db import models
from django.conf import settings


class Genre(models.Model):
    id = models.IntegerField(primary_key=True) # 장르 ID
    name = models.CharField(max_length=50)


class Actor(models.Model):
    id = models.IntegerField(primary_key=True) # 배우 ID
    name = models.CharField(max_length=100)
    character = models.CharField(max_length=100) # 역할
    profile_path = models.TextField()


class Movie(models.Model):
    id = models.IntegerField(primary_key=True) # 영화 ID
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    title = models.CharField(max_length=100)
    overview = models.TextField() # 내용
    popularity = models.FloatField() # 인기도
    poster_path = models.TextField() # 포스터 주소
    release_date = models.DateTimeField() # 개봉일
    vote_average = models.FloatField() # 평점
    vote_count = models.IntegerField() # 평점 투표 수
    # runtime = models.Field() # 상영 시간
    genres = models.ManyToManyField(Genre) # 해당 영화의 장르
    actors = models.ManyToManyField(Actor) # 해당 영화의 배우



class Director(models.Model):
    id = models.IntegerField(primary_key=True) 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_path = models.TextField()


class Rank(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.FloatField()




    

