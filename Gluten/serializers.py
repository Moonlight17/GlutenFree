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
    quantity = serializers.CharField(source='profile.quantity')
    username = serializers.CharField()
    class Meta:
        model = Profile
        fields = ('id', 'username', 'avatar', 'quantity')


class ListReceptSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%B-%d")
    creater = UserSerializer()
    tag_name = TagSerializer(many=True,)
    class Meta:
        model = Recept
        fields = ('id', 'title', 'pub_date', 'creater', 'tag_name')

class ListCurrentReceptSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%m-%d   %H:%M:%S")
    creater = UserSerializer()
    tag_name = TagSerializer(many=True,)
    class Meta:
        model = Recept
        fields = ('id', 'title', 'recepts_text', 'pub_date', 'creater', 'tag_name')



class TagSerializer(serializers.ModelSerializer):

    # recepts_text = serializers.JSONField(binary=True)
    class Meta:
        model = Tag
        fields = ('id', 'name')

class AddReceptSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%m-%d  %H:%M:%S")
    tag_name = TagSerializer(many=True,)
    creater = UserSerializer()
    class Meta:
        model = Recept
        fields = ('id', 'title', 'recepts_text', 'pub_date', 'creater', 'tag_name')