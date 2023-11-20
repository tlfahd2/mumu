from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('sort/<int:sort_num>/', views.movie_list),
    path('detail/<int:movie_id>/', views.movie_detail),
    path('genres/', views.genre_list),
    path('data/', views.create_data),
    path('<int:movie_pk>/reviews/', views.review_list), # 영화 관련 리뷰
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail),
    path('<int:movie_pk>/reviews/<int:review_pk>/comments/', views.review_comments), # 리뷰에 대한 댓글
    path('<int:movie_pk>/reviews/<int:review_pk>/comments/<int:comment_pk>', views.review_comment),
]