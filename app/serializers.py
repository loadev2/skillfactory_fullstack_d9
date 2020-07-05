from app.models import Post, Category
from rest_framework import serializers
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class CategorySerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    category = CategorySerializerShort(required=False)

    class Meta:
        model = Post
        fields = '__all__'


class PostSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']


class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializerShort(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'posts']

class CategorySerializerDetailed(serializers.ModelSerializer):
    posts = PostSerializerShort(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'posts']
