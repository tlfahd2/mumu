from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser
from allauth.account.adapter import get_adapter

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    day = serializers.IntegerField()
    gender = serializers.CharField(max_length=5)
    
    class Meta:
        model = CustomUser
        fields = '__all__'
    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'name': self.validated_data.get('name'),
            'year': self.validated_data.get('year'),
            'month': self.validated_data.get('month'),
            'day': self.validated_data.get('day'),
            'gender': self.validated_data.get('gender'),
        }
        
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.name = self.cleaned_data.get('name')
        user.year = self.cleaned_data('year')
        user.month = self.cleaned_data('month')
        user.day = self.cleaned_data('day')
        user.gender = self.cleaned_data('gender')
        return user
        