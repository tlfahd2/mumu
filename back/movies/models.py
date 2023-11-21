from django.db import models

from django.conf import settings


class Genre(models.Model):
    id = models.IntegerField(primary_key=True) # 장르 ID
    name = models.CharField(max_length=50)


class Actor(models.Model):
    id = models.IntegerField(primary_key=True) # 배우 ID
    name = models.CharField(max_length=100)
    profile_path = models.TextField(null=True, blank=True)
    another_name = models.TextField(null=True, blank=True)


class Director(models.Model):
    id = models.IntegerField(primary_key=True) 
    name = models.CharField(max_length=100)
    profile_path = models.TextField(null=True, blank=True)


class Movie(models.Model):
    id = models.IntegerField(primary_key=True) # 영화 ID
    adult = models.BooleanField()
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True, blank=True) # 내용
    popularity = models.FloatField(null=True, blank=True) # 인기도
    poster_path = models.TextField(null=True, blank=True) # 포스터 주소
    release_date = models.DateField(null=True, blank=True) # 개봉일
    runtime = models.IntegerField(null=True, blank=True) # 상영 시간
    vote_average = models.FloatField(null=True, blank=True) # 평점
    vote_count = models.IntegerField(null=True, blank=True) # 평점 투표 수
    trailer = models.TextField(null=True, blank=True)
    genres = models.ManyToManyField(Genre) # 해당 영화의 장르
    actors = models.ManyToManyField(Actor) # 해당 영화의 배우
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True) # 해당 영화 좋아요 누른 유저 정보 

# 영화에 대한 리뷰 게시판
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='hate_users')
    content = models.CharField(max_length=200)
    rank = models.FloatField()
    is_like = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review_comment_user')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# class Character(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='actor_character')
#     character = models.CharField(max_length=100)



# class Rank(models.Model):
#     review = models.ForeignKey(Review, on_delete=models.CASCADE)
#     score = models.FloatField()




    

