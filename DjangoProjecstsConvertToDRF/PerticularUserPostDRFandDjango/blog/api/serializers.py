from pydoc import importfile
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)
from blog.models import Post
from users.api.serializsers import ProfileSerializer
# from users.models import Profile


class PostCreateSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'title', 'content', 'date_posted', 'author'
        ]

    author = SerializerMethodField()

    def get_author(self, obj):
        return obj.author.username


class PostListSerializer(ModelSerializer):
    # author = ProfileSerializer()
    author = SerializerMethodField()

    def get_author(self, obj):
        return obj.author.username

    detail_url = HyperlinkedIdentityField(
        view_name='detail',
        lookup_field='pk'
    )
    
    author = HyperlinkedIdentityField(
        view_name='particular-user-posts',
        lookup_field='author'
    )

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'date_posted', 'author', 'detail_url'
        ]

    # author = SerializerMethodField()

    # def get_author(self, obj):
    #     return obj.author.username


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'date_posted', 'author'
        ]

    author = SerializerMethodField()

    def get_author(self, obj):
        return obj.author.username


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'date_posted', 'author'
        ]
    author = SerializerMethodField()

    def get_author(self, obj):
        return obj.author.username
