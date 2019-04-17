from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions
from django.core import serializers
import json
from .models import *


from .serializers import ListReceptSerializer, AddReceptSerializer, ListCurrentReceptSerializer, TagSerializer, UserSerializer, AddCommentSerializer, ListCommentSerializer


class ListRecept(APIView):
    # permission_classes = [permissions.IsAuthenticated, ] #for avtorise
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, count):
        recepts = Recept.objects.all().order_by('-pub_date')[count:count + 9]
        serializer = ListReceptSerializer(recepts, many=True)
        data = serializer.data[:]
        return Response(data)


class TagLoad(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)
        data = serializer.data[:]
        return Response(data)


class UserCurrentLoad(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, id):
        data = []
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        cur_user = serializer.data
        recepts = Recept.objects.filter(creater_id = user)
        serializer = ListReceptSerializer(recepts, many=True)
        recepts = serializer.data
        data.append(
			{
				'user': cur_user,
				'recepts': recepts
			}
        )
        return Response(data)




class ListCurrentRecept(CreateAPIView):
    serializer_class = ListCurrentReceptSerializer(many=True)
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, id):
        recept = Recept.objects.filter(pk=id)
        # print(type(recept['recepts_text']))
        serializer = ListCurrentReceptSerializer(recept, many=True)
        dataRecept = serializer.data[:]
        return Response(dataRecept)


class ListCurrentComments(CreateAPIView):
    serializer_class = ListCurrentReceptSerializer(many=True)
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, id, count):
        comm = Comment.objects.filter(recept=id).order_by('-pub_date')[count:count + 9]
        comm_data = ListCommentSerializer(comm, many=True)
        dataComment = comm_data.data[:]
        print(dataComment)
        return Response(dataComment)



class AddRecept(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ] #for avtorise
    serializer_class = AddReceptSerializer(many=True)
    model = Recept

    def post(self, request):
        
        data = json.loads(request.body.decode('utf-8'))
        Text = json.loads(data['Text'])
        Title = data['Title']
        Tag = data['Tag']
        if ( data['Title'] != '' and data['Text'] != '[]' and data['Tag'] != []):
            Creater = User.objects.get(username=request.user)
            post = Recept()
            post.title = Title
            post.recepts_text = Text
            post.user = Creater
            post.save()
            for select_tag in Tag:
                print(select_tag)
                post.tag_name.add(select_tag['id'])
            rec = Recept.objects.filter(user=Creater).count()
            print(request.user)

            try:
                obj = Profile.objects.get(user=request.user)
            except Profile.DoesNotExist:
                obj = Profile(user=request.user, avatar='media/default.png', quantity = rec)
                obj.save()
            print(obj)
            print("New Recept")

        return Response(status=201)


class AddComment(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]  #for avtorise
    serializer_class = AddCommentSerializer(many=True)
    model = Comment

    def post(self, request):

        data = json.loads(request.body.decode('utf-8'))
        Text = data['Text']
        Recept_id = data['Recept_id']
        ReceptEntry = Recept.objects.get(id=Recept_id)
        Creater = User.objects.get(username=request.user)
        like = LikeRecept.objects.filter(recept=ReceptEntry).count()
        comm = Comment()
        comm.recept = ReceptEntry
        comm.text = Text
        comm.user = Creater
        comm.likes = like
        comm.save()
        
        print("New Comment")

        return Response(status=201)




