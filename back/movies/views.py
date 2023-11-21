import requests, json
from datetime import date
from django.conf import settings
from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# 인증된 사람들만 가능하도록
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Genre
from .serializers import MovieListSerializer, GenreSerializer
from community.models import Review, Comment
from community.serializers import ReviewSerializer, CommentSerializer


# 영화 리스트 함수
@api_view(['GET'])
def movie_list(request, sort_num):
    if request.method == 'GET':
        if sort_num == 1: # 인기도순
            populars = Movie.objects.filter(release_date__lte=date.today()).order_by('-popularity')[:500]
            serializers = MovieListSerializer(populars, many=True)
        elif sort_num == 2: # 최신 - 인기 순 개봉이 된 영화들만
            movies = Movie.objects.filter(release_date__lte=date.today()).order_by('-release_date','popularity')[:500]
            serializers = MovieListSerializer(movies, many=True)
        elif sort_num == 3:
            pass
        elif sort_num == 4:
            movies = Movie.objects.filter(release_date__gt=date.today()).order_by('release_date', '-popularity')
            serializers = MovieListSerializer(movies, many=True)
        elif sort_num in [12, 14, 16, 18, 27, 28, 35, 36, 37, 53, 80, 99, 878, 9648, 10402, 10749, 10751, 10752, 10770]:
            genre = get_object_or_404(Genre, pk=sort_num)
            movies = genre.movie_set.all().order_by('-popularity')
            serializers = MovieListSerializer(movies, many=True)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


        return Response(serializers.data)

             
@api_view(["GET"])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializers = GenreSerializer(genres, many =True)
    return Response(serializers.data)

# 영화 상세 함수
@api_view(['GET'])
def movie_detail(request, movie_id):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieListSerializer(movie)
        return Response(serializer.data)

# 영화 리뷰 
@api_view(["GET", "POST"])
def review_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    if request.method == 'GET':
        reviews = movie.review_set.all()
        serializers = ReviewSerializer(reviews, many= True)
        return Response(serializers.data)
    elif request.method == "POST":
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
           serializer.save(movie=movie)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
      


@api_view(["GET"])
def review_detail(request, review_pk):
    if request.method == "GET":
        review = get_object_or_404(Review, pk=review_pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def review_comments(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        comments = review.comment_set.all()
        serializers = CommentSerializer(comments, many= True)
        return Response(serializers.data)
    elif request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
           serializer.save(review=review)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
   


@api_view(["GET"])
def review_comment(request, review_pk, comment_pk):
   pass




# 영화 관련 데이터를 받아와서 제이슨으로 저장 하는 함수
# 관리자만 실행할 수 있도록 권한을 주어야 함
def create_data(request):
    TMDB_API = settings.TMDB_API
    BASE_URL = 'https://api.themoviedb.org/3'
    
    # 영화에 대한 정보
    total_data = []
    # 배우에 대한 정보저장 배열과 중복 체크 배열까지
    actor_dup = []
    # 감독에 대한 정보 중복인지 체크할 배열까지
    director_dup = []  
    # 장르 데이터 받아오기                                                                                                                                                                                                    
    request_url_gerne = f"{BASE_URL}/genre/movie/list?api_key={TMDB_API}&language=ko-KR"
    genres = requests.get(request_url_gerne).json()
    for genre in genres['genres']:
        fields = {
            'name' : genre['name']
        }
        data = {
            'model':"movies.Genre",
            "pk":genre["id"],
            "fields":fields
        }
        total_data.append(data)
    movies = []
    # 개봉 예정작 160개 가져오기
    for page in range(1, 8):
        request_url_upcoming = f"{BASE_URL}/movie/upcoming?api_key={TMDB_API}&language=ko-KR&page={page}"
        upcoming = requests.get(request_url_upcoming).json()
        movies += upcoming['results']
    # 인기 영화 중 상위 10000개 데이터 가져오기 1page당 20개의 데이터
    for page in range(1, 10):
        request_url_movies = f"{BASE_URL}/movie/popular?api_key={TMDB_API}&language=ko-KR&page={page}"
        popular = requests.get(request_url_movies).json()
        movies += popular['results']
    print(len(movies))

    # 해당 영화에 하나씩 접근해서 영화 정보 저장
    for movie in movies:
        # 영화 정보 중 포스터 정보가 없다면 해당 데이터는 저장 하지 않는다.
        if movie.get('poster_path') == '' or movie.get('overview') == '':
            continue
        # 해당 영화 상세 정보와 감독/출연자 정보 api 신청
        request_url_movie = f"{BASE_URL}/movie/{movie['id']}?api_key={TMDB_API}&language=ko-KR"
        request_url_credits=f"{BASE_URL}/movie/{movie['id']}/credits?api_key={TMDB_API}&language=ko-KR"
        request_url_video = f"{BASE_URL}/movie/{movie['id']}/videos?api_key={TMDB_API}&language=ko-KR"
        persons = requests.get(request_url_credits).json()
        moviedetail = requests.get(request_url_movie).json()
        videos = requests.get(request_url_video).json()
        # 관련 영상이 있다면
        # 예고편 키 초기화
        video_key = ''
        if videos['results']:
            for video in videos['results']:
                # 해당 영상이 유튜브 영상이고 예고편 타입이라면 저장
                if video.get('site') =='YouTube' and video.get('type') == 'Trailer' or video.get('type') == 'Teaser':
                    video_key = video['key']
                    break
        # credits에서 뽑아온 사람들 중에 crew 키의 값 중 Director인 사람 director에 저장
        crew = persons['crew']
        for person in crew:
            if person['job'] == 'Director':
                director_id = person['id']
                if director_id not in director_dup:
                    fields = {
                        'name' : person['name'],
                        'profile_path': person['profile_path'],
                    }
                    data = {
                        'model' : 'movies.Director',
                        'pk' : director_id,
                        'fields' : fields
                    }
                    total_data.append(data)
                    break
        
        # credits에서 cast 키 값으로 가져온 주연 배우 10명
        main_actors = persons['cast'][:10]
            # 영화 데이터에 넣어줄 배우 id 목록 영화마다 초기화
        movie_actor_id = []
        for actor in main_actors:
            # 해당 영화의 배우 id 목록에 넣어주지
            movie_actor_id.append(actor['id'])
            # 배우 모델을 만들어줄 데이터 목록
            if actor['id'] not in actor_dup:
                fields = {
                        'name' : actor['name'],
                        'profile_path': actor['profile_path'],
                }
                data = {
                    'model' : 'movies.Actor',
                    'pk' : actor['id'],
                    'fields' : fields
                }
                total_data.append(data)
            
        fields = {
            'adult' : moviedetail['adult'],
            'title' : moviedetail['title'],
            'overview' : moviedetail['overview'],
            'popularity' : moviedetail['popularity'],
            'poster_path' : moviedetail['poster_path'],
            'release_date' : moviedetail['release_date'],
            'runtime' : moviedetail['runtime'],
            'vote_average' : moviedetail['vote_average'],
            'vote_count' : moviedetail['vote_count'],
            'trailer': video_key,
            'genres' : movie['genre_ids'],
            'actors' : movie_actor_id,
            'director' : director_id,
            'like_users' : []
        }
        data ={
            'model' : 'movies.Movie',
            'pk' : movie['id'],
            'fields' : fields
        }
        total_data.append(data)
    save_dir = '../back/movies/fixtures/movies_data.json'    
    with open(save_dir, "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=2, ensure_ascii=False)
        
    return Response('데이터 받기 완료', status=status.HTTP_200_OK)