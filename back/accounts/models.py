from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=50)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=5)
    
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    
    # 리스트 데이터 저장을 위해 text형태로 저장
    movie_users = models.TextField(blank=True, null=True)
    
    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    
    
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_email, user_field, user_username
        
        data = form.cleaned_data
        username = data.get("username")
        name = data.get("name")
        year = data.get("year")
        month = data.get("month")
        day = data.get("day")
        gender = data.get("gender")
        email = data.get("email")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        movie_user = data.get("movie_users")
        
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if name:
            user.name = name
        if year:
            user.year = year
        if month:
            user.month = month
        if day:
            user.day = day
        if gender:
            user.gender = gender
        if movie_user:
            movie_users = user.movie_users.split(',')
            movie_users.append(movie_user)
            if len(movie_users) > 1:
                movie_users = ','.join(movie_users)
            user_field(user, "movie_users", movie_users)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user
    
    