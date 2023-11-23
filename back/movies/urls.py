from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('sort/<int:sort_num>/page/<int:page_num>', views.movie_list),
    path('detail/<int:movie_id>/', views.movie_detail),
    path('genres/', views.genre_list),
    path('data/', views.create_data),
    path('search/<str:keyword>/', views.search_movie),
    path('reviews/', views.review_list), # 모든 리뷰 목록 조회
    path('reviews/<int:review_pk>/', views.review_detail),
    path('<int:movie_pk>/reviews/', views.movie_review_list), # 해당 영화와 관련된 영화 정보
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.movie_review_detail),
    path('like_movies/<int:movie_pk>/<int:user_pk>/', views.like_movies), # 영화 좋아요
    path('like_reviews/<int:review_pk>/<int:user_pk>/', views.like_reviews), # 리뷰 좋아요
    path('hate_reviews/<int:review_pk>/<int:user_pk>/', views.hate_reviews), # 리뷰 싫어요
]