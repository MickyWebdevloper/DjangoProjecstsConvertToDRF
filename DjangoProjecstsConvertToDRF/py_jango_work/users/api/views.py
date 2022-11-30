from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView
)
from . serializsers import (
    UserCreateSerializer,
    UserLoginSerializer,
    ProfileSerializer
)
from blog.models import Post
from .permissions import IsPostOwner


class UserRegisterApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserLoginApiView(APIView):
    queryset = Post.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, format=None):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        # serializer.save()
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



from rest_framework.generics import (
    RetrieveUpdateAPIView
)
from users.models import Profile
# User's Profile view here
class ProfileView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsPostOwner]

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user)
