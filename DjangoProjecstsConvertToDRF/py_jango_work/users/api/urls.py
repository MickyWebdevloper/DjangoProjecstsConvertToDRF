from django.urls import path
from . views import (
    UserLoginApiView,
    UserRegisterApiView,
    ProfileView
)

urlpatterns = [
    path('register/', UserRegisterApiView.as_view(), name='register-user'),
    path('login/', UserLoginApiView.as_view(), name='login-user'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile-user'),
]
