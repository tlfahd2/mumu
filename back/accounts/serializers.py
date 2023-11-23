from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User
from movies.models import Movie
from movies.models import Review
from allauth.account.adapter import get_adapter

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    day = serializers.IntegerField()
    gender = serializers.CharField(max_length=5)
    music = serializers.CharField(max_length=50)
    
    class Meta:
        model = User
        fields = '__all__'
    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'name': self.validated_data.get('name'),
            'year': self.validated_data.get('year'),
            'month': self.validated_data.get('month'),
            'day': self.validated_data.get('day'),
            'gender': self.validated_data.get('gender'),
            'music': self.validated_data.get('music'),
        }
        
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        # user.name = self.cleaned_data.get('name')
        # user.year = self.cleaned_data('year')
        # user.month = self.cleaned_data('month')
        # user.day = self.cleaned_data('day')
        # user.gender = self.cleaned_data('gender')
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user


class UserSerializer(serializers.ModelSerializer):
    class FollowSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id','username',)
    followers = FollowSerializer(many=True)
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'
    like_movies = MovieSerializer(many=True)
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = '__all__'
    like_reviews = ReviewSerializer(many=True)
    hate_reviews = ReviewSerializer(many=True)
    class Meta:
        model = User
        fields = ('__all__')
        read_only_fields = ('followings', 'like_movies', 'followers', 'like_reviews', 'hate_reviews',)
