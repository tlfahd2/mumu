from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .models import User

@api_view(['POST', 'GET'])
def FollowView(request, user_id):
    if request.method == 'POST':
        you = get_object_or_404(User, id=user_id)
        me = request.user
        if me in you.followers.all():
            you.followers.remove(me)
            me.followings.remove(you)
            return Response('팔로우취소',status=status.HTTP_200_OK)
        else:
            you.followers.add(me)
            me.followings.add(you)
            return Response('팔로우완료',status=status.HTTP_200_OK)
    
    elif request.method == 'GET':
        you = get_object_or_404(User, id=user_id)
        followers = you.followers.all()
        followers_length = len(followers)
        return Response(followers_length)

@api_view(['GET'])
def FollowingView(request, user_id):
        you = get_object_or_404(User, id=user_id)
        followings = you.followings.all()
        followings_length = len(followings)
        return Response(followings_length)