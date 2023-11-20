from datetime import date
from django.conf import settings
from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Article, Review, Comment
from .serializers import ArticleSerializer, ReviewSerializer, CommentSerializer


@api_view(["GET", "POST"])
def article_list(request):
    if request.method == 'GET':
      articles = get_list_or_404(Article)
      serializers = ArticleSerializer(articles, many= True)
      return Response(serializers.data)
    elif request.method == "POST":
       serializer = ArticleSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      

@api_view(["GET"])
def article_detail(request, article_pk):
   pass


@api_view(["GET"])
def article_comments(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if request.method == 'GET':
      comments = get_list_or_404(Comment)
      serializers = CommentSerializer(comments, many= True)
      return Response(serializers.data)
    elif request.method == "POST":
       serializer = ArticleSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
          serializer.save(article=article)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      

@api_view(["GET", "PUT","DELETE"])
def article_comment(request, article_pk, comment_pk):
   pass



