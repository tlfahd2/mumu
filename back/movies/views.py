import requests, json
from django.conf import settings
from django.shortcuts import render
from rest_framework.response import Response  
from rest_framework.decorators import permission_classes
# 인증된 사람들만 가능하도록
from rest_framework.permissions import IsAuthenticated



# 영화 관련 데이터를 받아와서 제이슨으로 저장 하는 함수
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
            'model':"movies.genre",
            "pk":genre["id"],
            "fields":fields
        }
        total_data.append(data)
    # 인기 영화 중 상위 10000개 데이터 가져오기 1page당 20개의 데이터
    for page in range(1, 10):
        request_url_movie = f"{BASE_URL}/movie/popular?api_key={TMDB_API}&language=ko-KR&page={page}"
        movies = requests.get(request_url_movie).json()

        # 해당 영화에 하나씩 접근해서 영화 정보 저장
        for movie in movies['results']:
            # 해당 영화에 출연하는 감독, 배우를 찾기 위한 url
            request_url_credits=f"{BASE_URL}/movie/{movie['id']}/credits?api_key={TMDB_API}&language=ko-KR"
            persons = requests.get(request_url_credits).json()
            # credits에서 뽑아온 사람들 중에 crew 키의 값 중 Director인 사람 dirtors에 저장
            crew = persons['crew']
            for person in crew:
                if person['job'] == 'Director':
                    director_id = person['id']
                    if director_id not in director_dup:
                        fields = {
                            'name' : person['name'],
                            'profile_path': person['profile_path'],
                            'movie' : movie['id']
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
                # 해당 배우의 배역 저장
                fields={
                    'movie': movie['id'],
                    'actor': actor['id'],
                    'character': actor['character']
                }
                data = {
                    'model' : 'movies.Character',
                    'fields' : fields
                }
                total_data.append(data)
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
                'title' : movie['title'],
                'overview' : movie['overview'],
                'popularity' : movie['popularity'],
                'poster_path' : movie['poster_path'],
                'release_date' : movie['release_date'],
                'vote_average' : movie['vote_average'],
                'vote_count' : movie['vote_count'],
                # 'runtime' : movie['runtime'],
                'genres' : movie['genre_ids'],
                'actors' : movie_actor_id,
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
    return Response(f'영화 데이터 업로드 완료')

    

# Create your views here.
@permission_classes([IsAuthenticated])
def movie_list(request):
    pass

