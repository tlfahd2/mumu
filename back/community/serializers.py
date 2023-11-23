from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class userNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username',)
    user = userNameSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class userNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username',)
    user = userNameSerializer(read_only=True)
    article = ArticleSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'



