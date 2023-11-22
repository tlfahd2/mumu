from rest_framework import serializers
from .models import Movie, Director, Actor, Genre, Review, Comment
from accounts.models import User


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('name', 'profile_path','another_name')


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name', 'profile_path','another_name')


# class CharacterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Character
#         fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    director = DirectorSerializer()
    actors = ActorSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class userNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username',)
    user = userNameSerializer(read_only=True)
    class movieNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path',)
    movie = movieNameSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('__all__')
        read_only_fields = ('like_users', 'hate_users', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
