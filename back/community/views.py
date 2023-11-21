from datetime import date
from django.conf import settings
from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer


@api_view(["GET", "POST"])
def article_list(request):
   if request.method == 'GET':
      articles = Article.objects.all().order_by('-updated_at')
      serializers = ArticleSerializer(articles, many= True)
      return Response(serializers.data)
   elif request.method == "POST":
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
         serializer.save(user=request.user)
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      

@api_view(["GET", "PUT", "DELETE"])
def article_detail(request, article_pk):
   article = get_object_or_404(Article, pk=article_pk)
   if request.method == 'GET':
      serializer = ArticleSerializer(article)
      return Response(serializer.data)
   elif request.method == "PUT":
      serializer = ArticleSerializer(article, data=request.data)
      if serializer.is_valid(raise_exception=True):
         serializer.save()
         return Response(serializer.data)
   elif request.method == 'DELETE':
      article.delete()
      return Response(f"{article_pk}번 게시글 삭제", status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def article_comments(request, article_pk):
   print(request.data, request.user)
   article = get_object_or_404(Article, pk = article_pk)
   if request.method == 'GET':
      # 생성일 기준으로 정렬해서 반환
      comments = article.article_comments.order_by('-created_at')
      serializers = CommentSerializer(comments, many= True)
      return Response(serializers.data)
   elif request.method == "POST":
      serializer = CommentSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
         print(serializer, request.user)
         serializer.save(user=request.user, article=article)
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      

@api_view(["PUT","DELETE"])
def article_comment(request, article_pk, comment_pk):
   pass



