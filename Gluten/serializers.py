from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source='profile.avatar')
    quantity = serializers.IntegerField(source='profile.quantity')
    username = serializers.CharField()
    class Meta:
        model = Profile
        fields = ('id', 'username', 'avatar', 'quantity')


class ListReceptSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%B-%d")
    user = UserSerializer()
    tag_name = TagSerializer(many=True,)
    class Meta:
        model = Recept
        fields = ('id', 'title', 'pub_date', 'user', 'tag_name')

class ListCurrentReceptSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%m-%d   %H:%M:%S")
    user = UserSerializer()
    tag_name = TagSerializer(many=True,)
    class Meta:
        model = Recept
        fields = ('id', 'title', 'recepts_text', 'pub_date', 'user', 'tag_name')

class ListCommentSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%m-%d   %H:%M:%S")
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ('id', 'text', 'pub_date', 'user', 'likes')



class TagSerializer(serializers.ModelSerializer):

    # recepts_text = serializers.JSONField(binary=True)
    class Meta:
        model = Tag
        fields = ('id', 'name')

class AddReceptSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%m-%d  %H:%M:%S")
    tag_name = TagSerializer(many=True,)
    user = UserSerializer()
    class Meta:
        model = Recept
        fields = ('id', 'title', 'recepts_text', 'pub_date', 'user', 'tag_name')

class AddCommentSerializer(serializers.ModelSerializer):
    recept = ListCurrentReceptSerializer()
    pub_date = serializers.DateTimeField(format="%Y-%m-%d  %H:%M:%S")
    user = UserSerializer()
    class Meta:
        model = Recept
        fields = ('id', 'recept', 'text', 'pub_date', 'user', 'likes')