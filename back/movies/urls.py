from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('<int:sort_num>/', views.movie_list),
    path('detail/<int:movie_id>/', views.movie_detail),
    path('genres/', views.genre_list),
    path('data/', views.create_data),
]