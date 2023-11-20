from django.db import models
from movies.models import Movie
from django.conf import settings

# 자유 게시판 구현 
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    content = models.TextField()


# 영화에 대한 리뷰 게시판
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='hate_users')
    content = models.CharField(max_length=200)
    rank = models.FloatField()
    is_like = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
