from django.shortcuts import render
from rest_framework.decorators import permission_classes
# 인증된 사람들만 가능하도록
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@permission_classes([IsAuthenticated])
def movie_list(request):
    pass

