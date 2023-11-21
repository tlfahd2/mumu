from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('sort/<int:sort_num>/', views.movie_list),
    path('detail/<int:movie_id>/', views.movie_detail),
    path('genres/', views.genre_list),
    path('data/', views.create_data),
    path('reviews/', views.review_list), # 모든 리뷰 목록 조회
    path('<int:movie_pk>/reviews/', views.movie_review_list), # 해당 영화와 관련된 영화 정보
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail),
    path('<int:movie_pk>/reviews/<int:review_pk>/comments/', views.review_comments), # 리뷰에 대한 댓글
    path('<int:movie_pk>/reviews/<int:review_pk>/comments/<int:comment_pk>', views.review_comment),
    path('like/<int:movie_pk>/<int:user_pk>/', views.like_movies), # 영화 좋아요
]