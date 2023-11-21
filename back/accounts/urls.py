from django.urls import path
from . import views

urlpatterns = [
    path('follow/<int:my_pk>/<str:username>/', views.follow),
    path('<str:username>/', views.profile)
]
