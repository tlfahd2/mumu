from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer
from rest_framework.response import Response
# Create your views here.

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        response_data = self.get_response_data(user)
        return Response(response_data, status=201)