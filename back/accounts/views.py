from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def follow(request, my_pk, username):
    you = get_object_or_404(User, username=username)
    me = get_object_or_404(User, pk=my_pk)
    if you != me:
        if me.followings.filter(pk=you.pk).exists():
            me.followings.remove(you)
            following = False
        else:
            me.followings.add(you)
            following = True
        return Response(following)
    
