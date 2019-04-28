from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class ImageReceptSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Gallery
        fields = ('id', 'image')


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source='profile.avatar')
    quantity = serializers.IntegerField(source='profile.quantity')
    username = serializers.CharField()
    class Meta:
        model = Profile
        fields = ('id', 'username', 'avatar', 'quantity')

class ListUserReceptSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%B-%d")
    user = UserSerializer()
    tag_name = TagSerializer()
    like = serializers.SerializerMethodField('has_like')
    class Meta:
        model = Recept
        fields = ('id', 'title', 'pub_date', 'user', 'tag_name', 'likes', 'like')
        
    def has_like(self, obj):
        """Check for whether the visiting user fav'd the story.
        """

        user = self.context['request'].user
        recept = obj # the story object
        # user_like_post = False # False by default
        return bool(LikeRecept.objects.filter(user=user.id, recept=recept.id)  )



class ListReceptSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%B-%d")
    user = UserSerializer()
    tag_name = TagSerializer()
    class Meta:
        model = Recept
        fields = ('id', 'title', 'pub_date', 'user', 'tag_name', 'likes')

class ListCurrentReceptSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%m-%d   %H:%M:%S")
    user = UserSerializer()
    tag_name = TagSerializer(many=True,)
    class Meta:
        model = Recept
        fields = ('id', 'title', 'comp', 'text', 'pub_date', 'user', 'tag_name', 'likes')

class AuthListCurrentReceptSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%m-%d   %H:%M:%S")
    user = UserSerializer()
    tag_name = TagSerializer(many=True,)
    like = serializers.SerializerMethodField('has_like')
    class Meta:
        model = Recept
        fields = ('id', 'title', 'comp', 'text', 'pub_date', 'user', 'tag_name', 'like', 'likes')

    def has_like(self, obj):
        """Check for whether the visiting user fav'd the story.
        """
        user = self.context['request'].user
        recept = obj # the story object
        # user_like_post = False # False by default
        return bool(LikeRecept.objects.filter(user=user.id, recept=recept.id))


class ListCommentSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%m-%d   %H:%M:%S")
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ('id', 'text', 'pub_date', 'user', 'likes')

class AuthListCommentSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%m-%d   %H:%M:%S")
    user = UserSerializer()
    like = serializers.SerializerMethodField('has_like')
    class Meta:
        model = Comment
        fields = ('id', 'text', 'pub_date', 'user', 'likes', 'like')

    def has_like(self, obj):
        """Check for whether the visiting user fav'd the story.
        """

        user = self.context['request'].user
        comm = obj # the story object
        # user_like_post = False # False by default
        return bool(LikeComment.objects.filter(user=user.id, recept=comm.recept, comment=comm.id))


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
        fields = ('id', 'title', 'comp', 'text', 'pub_date', 'user', 'tag_name')

class AddCommentSerializer(serializers.ModelSerializer):
    recept = ListCurrentReceptSerializer()
    pub_date = serializers.DateTimeField(format="%Y-%m-%d  %H:%M:%S")
    user = UserSerializer()
    class Meta:
        model = Recept
        fields = ('id', 'recept', 'text', 'pub_date', 'user', 'likes')