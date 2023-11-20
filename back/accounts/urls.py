from django.urls import path
from . import views

urlpatterns = [
    path('follow/<int:user_id>/', views.FollowView),
    path('following/<int:user_id>/', views.FollowingView)
]
