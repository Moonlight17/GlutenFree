from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions
from django.core import serializers
import json
from .models import *


from .serializers import ListReceptSerializer, AddReceptSerializer, ListCurrentReceptSerializer, TagSerializer


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




class ListCurrentRecept(CreateAPIView):
    serializer_class = ListCurrentReceptSerializer(many=True)
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, id):
        recept = Recept.objects.filter(pk=id)
        # print(type(recept['recepts_text']))
        serializer = ListCurrentReceptSerializer(recept, many=True)
        data = serializer.data[:]
        # print(type(data['recepts_text']))
        return Response(data)

class AddRecept(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ] #for avtorise
    serializer_class = AddReceptSerializer(many=True)
    model = Recept

    def post(self, request):
        
        data = json.loads(request.body.decode('utf-8'))
        Text = json.loads(data['Text'])
        Title = data['Title']
        Tag = data['Tag']
        if ( data['Title'] != '' and data['Text'] != [] and data['Tag'] != []):
            Creater = User.objects.get(username=request.user)
            post = Recept()
            post.title = Title
            post.recepts_text = Text
            post.creater = Creater
            post.save()
            for select_tag in Tag:
                print(select_tag)
                post.tag_name.add(select_tag['id'])
            rec = Recept.objects.filter(creater=Creater).count()
            print(rec)
            Creater.quantity = rec
            Creater.save()
            QuaUser = Profile.objects.get(user=request.user)
            QuaUser.quantity = rec
            QuaUser.save()
            print("New Recept")

        return Response(status=201)





