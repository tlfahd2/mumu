from rest_framework import serializers
from .models import Movie, Director, Actor, Character, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('name', 'profile_path')


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name', 'profile_path')


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    director = DirectorSerializer()
    actors = ActorSerializer(many=True)
    character_set = CharacterSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'
