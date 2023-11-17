from django.conf import settings
import requests

TMDB_API=settings.TMDB_API
BASE_URL = 'https://api.themoviedb.org/3'
def get_total_datas():
    movies = []
    actors = []
    directors = []
    # 장르 데이터 받아오기
    request_url_gerne = f"{BASE_URL}/genre/movie/list?api_key='{TMDB_API}&language=ko-KR"
    genres = requests.get(request_url_gerne).json()
    print(genres)

get_total_datas()

