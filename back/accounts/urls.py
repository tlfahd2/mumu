from django.urls import path
from . import views

urlpatterns = [
    path('follow/<int:user_id>/', views.FollowView.as_view()),
    path('following/<int:user_id>/', views.FollowingView.as_view())
]
