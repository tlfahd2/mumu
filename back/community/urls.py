from django.urls import path, include
from . import views


urlpatterns = [
    path('articles/', views.article_list), # 자유 게시글
    path('articles/<int:article_pk>/', views.article_detail),
    path('articles/<int:article_pk>/comments/', views.article_comments), # 자유 게시글에 대한 댓글
    path('articles/<int:article_pk>/comments/<int:comment_pk>/', views.article_comment),
]