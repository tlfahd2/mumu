from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .models import User

class FollowView(APIView):
    def post(self, request, user_id):
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
    
    def get(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        followers = you.followers.all()
        followers_length = len(followers)
        return Response(followers_length)
    
class FollowingView(APIView):
    def get(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        followings = you.followings.all()
        followings_length = len(followings)
        return Response(followings_length)