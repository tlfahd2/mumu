import requests, json, re
from datetime import date
from django.conf import settings
from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# 인증된 사람들만 가능하도록
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from .models import Movie, Genre, Review, Comment, Actor, Director
from .serializers import MovieListSerializer, GenreSerializer, ReviewSerializer, CommentSerializer
from accounts.models import User


# 영화 리스트 함수
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request, sort_num):
    if request.method == 'GET':
        if sort_num == 1: # 인기도순
            populars = Movie.objects.filter(release_date__lte=date.today()).order_by('-popularity')[:500]
            serializers = MovieListSerializer(populars, many=True)
        elif sort_num == 2: # 최신 - 인기 순 개봉이 된 영화들만
            movies = Movie.objects.filter(release_date__lte=date.today()).order_by('-release_date','popularity')[:500]
            serializers = MovieListSerializer(movies, many=True)
        elif sort_num == 3: # 맞춤 추천
            movies = []
            # 해당 유저가 좋아하는 음악 장르 추출 vue에서 문자열로 보내줌
            # 정규 표현식을 통해 단어들만 추출
            me = request.user
            music_genre = me.music
            user_genres = re.findall(r'"(.*?)"', music_genre)
            # 해당 유저가 좋아요를 누른 모든 영화 
            like_movies = me.like_movies.all()
            # 그 영화들을 좋아하는 다른 유저들 중 나의 음악 장르와 일치하는 사람들이 좋아요 한 영화 추천
            for movie in like_movies:
                for genre in user_genres:
                    users = movie.like_users.filter(music__icontains=genre)
                    movies = movies.union(users.like_movies.all())
            serializers = MovieListSerializer(movies, many=True)
            return Response(serializers.data)
        elif sort_num == 4: # 개봉 예정 영화 금일 부터 가깝고 인기가 많은 순으로 정렬
            movies = Movie.objects.filter(release_date__gt=date.today()).order_by('release_date', '-popularity')
            serializers = MovieListSerializer(movies, many=True)
        # 각 장르의 id에 맞춰 해당 장르를 역참조하여 인기도가 높은 순으로 정렬
        elif sort_num in [12, 14, 16, 18, 27, 28, 35, 36, 37, 53, 80, 99, 878, 9648, 10402, 10749, 10751, 10752, 10770]:
            genre = get_object_or_404(Genre, pk=sort_num)
            movies = genre.movie_set.all().order_by('-popularity')
            serializers = MovieListSerializer(movies, many=True)
        else:
            # 나머지로 들어오는 요청은 없는 요청 이므로 컨텐츠 없음을 반환 해준다.
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializers.data)


@api_view(["GET"])
def search_movie(request, keyword):
    # 검색한 키워드가 감독, 배우, 장르에 포함 되어 있는지 확인
    actors = Actor.objects.filter(name__icontains=keyword) | Actor.objects.filter(another_name__icontains=keyword)
    directors = Director.objects.filter(name__icontains=keyword) | Director.objects.filter(another_name__icontains=keyword)
    genres = Genre.objects.filter(name__icontains=keyword) 
    # 제목에 키워드가 있는 영화
    movies = Movie.objects.filter(title__icontains=keyword)
    # 내용에 키워드가 포함된 영화 추가해주기
    movies = movies.union(Movie.objects.filter(overview__icontains=keyword))
    # 검색한 단어가 포함된 배우들의 영화 정보 저장
    for actor in actors:
        movies = movies.union(actor.movie_set.all())
    for director in directors:
        movies = movies.union(director.movie_set.all())
    for genre in genres:
        movies = movies.union(genre.movie_set.all())
    movies = movies.order_by('-popularity')
    serializers = MovieListSerializer(movies, many=True)
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


# 전체 리뷰 조회 및 영화가 주어지지 않은 리뷰 생성 
@api_view(["GET", "POST"])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializers = ReviewSerializer(reviews, many= True)
        return Response(serializers.data)


# 영화별 리뷰 조회
@api_view(["GET", "POST"])
def movie_review_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        reviews = movie.review_set.all()
        serializers = ReviewSerializer(reviews, many= True)
        return Response(serializers.data)
    elif request.method == "POST":
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
           serializer.save(movie=movie)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
      

@api_view(["GET", "PUT", "DELETE"])
def review_detail(request, review_pk):
   review = get_object_or_404(Review, pk=review_pk)
   if request.method == 'GET':
      serializer = ReviewSerializer(review)
      return Response(serializer.data)
   elif request.method == "PUT":
      serializer = ReviewSerializer(review, data=request.data)
      if serializer.is_valid(raise_exception=True):
         serializer.save()
         return Response(serializer.data)
   elif request.method == 'DELETE':
      review.delete()
      return Response(f"{review_pk}번 게시글 삭제", status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# def review_comments(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     if request.method == 'GET':
#         comments = review.comment_set.all()
#         serializers = CommentSerializer(comments, many= True)
#         return Response(serializers.data)
#     elif request.method == "POST":
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#            serializer.save(review=review)
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
   


# @api_view(["GET"])
# def review_comment(request, review_pk, comment_pk):
#    pass


# 영화 좋아요
@api_view(["POST"])
def like_movies(request, movie_pk, user_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = get_object_or_404(User, pk=user_pk)
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        movie_like = False
    else:
        movie.like_users.add(user)
        movie_like = True
    return Response(movie_like)


# 리뷰 좋아요
@api_view(["POST"])
def like_reviews(request, review_pk, user_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = get_object_or_404(User, pk=user_pk)
    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        review_like = False
    else:
        review.like_users.add(user)
        review_like = True
    return Response(review_like)


# 리뷰 싫어요
@api_view(["POST"])
def hate_reviews(request, review_pk, user_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = get_object_or_404(User, pk=user_pk)
    if review.hate_users.filter(pk=user.pk).exists():
        review.hate_users.remove(user)
        review_hate = False
    else:
        review.hate_users.add(user)
        review_hate = True
    return Response(review_hate)


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
    for page in range(1, 50):
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
        for crew_person in crew:
            if crew_person['job'] == 'Director':
                request_url_person = f"{BASE_URL}/person/{crew_person['id']}?api_key={TMDB_API}&language=ko-KR"
                director = requests.get(request_url_person).json()
                director_id = director['id']
                if director_id not in director_dup:
                    anoter_name = ''
                    for na in director['also_known_as']:
                        name = re.sub('[^가-힣\s]', '', na).strip()
                        if name:
                            anoter_name = name
                            break
                    fields = {
                        'name' : director['name'],
                        'profile_path': director['profile_path'],
                        'another_name' : anoter_name,
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
        for cast_actor in main_actors:
            # 해당 영화의 배우 id 목록에 넣어주지
            movie_actor_id.append(cast_actor['id'])
            # 배우 모델을 만들어줄 데이터 목록
            if cast_actor['id'] not in actor_dup:
                # 영어 제외한 다른 이름도 있는지 확인
                request_url_actor = f"{BASE_URL}/person/{cast_actor['id']}?api_key={TMDB_API}&language=ko-KR"
                actor = requests.get(request_url_actor).json()
                anoter_name=''
                for na in actor['also_known_as']:
                    name = re.sub('[^가-힣\s]', '', na).strip()
                    if name:
                        anoter_name = name
                        break
                fields = {
                        'name' : actor['name'],
                        'profile_path': actor['profile_path'],
                        'another_name' : anoter_name,
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
    return Response({'msg' : '데이터 받기 완료'}, status=status.HTTP_200_OK)