from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions
from django.core import serializers
import json
from .models import *


from .serializers import ListReceptSerializer, AddReceptSerializer, ListCurrentReceptSerializer, AuthListCurrentReceptSerializer, TagSerializer, UserSerializer, MeUserSerializer, AddCommentSerializer, AuthListCommentSerializer, ListCommentSerializer, ListUserReceptSerializer, ImageReceptSerializer

# отображение всех записей
class ListRecept(APIView):
    # permission_classes = [permissions.IsAuthenticated, ] #for avtorise
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, count):
        # print(request.user)
        data = []
        if request.user.is_authenticated:
            recepts = Recept.objects.all().order_by('-pub_date')[count:count + 9]
            serializer = ListUserReceptSerializer(recepts, context={'request': request}, many=True)
            data = serializer.data[:]
        else:
            recepts = Recept.objects.all().order_by('-pub_date')[count:count + 9]
            serializer = ListReceptSerializer(recepts, context={'request': request}, many=True)
            data = serializer.data[:]
            # print(data)
        return Response(data)

# функция для добавления лайков на рецепты
class LikeRec(APIView):
    permission_classes = [permissions.IsAuthenticated,]  #for avtorise
    
    def get(self, request, id):
        # print(request.user)
        obj, created = LikeRecept.objects.get_or_create(user=request.user, recept_id=id)
        # print(obj)
        # print(created)
        if (not created):
            obj.delete()
        data = []
        return Response(data)

# функция для добавления лайков на рецепты

class LikeComm(APIView):
    permission_classes = [permissions.IsAuthenticated,]  #for avtorise
    
    def get(self, request, id, comm_id):
        # print(request.user)
        obj, created = LikeComment.objects.get_or_create(user=request.user, recept_id=id, comment_id = comm_id)
        # print(obj)
        # print(created)
        if (not created):
            obj.delete()
        data = []
        return Response(data)

# подгрузка тэгов
class TagLoad(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)
        data = serializer.data[:]
        return Response(data)

# информация об определенном пользователе
class UserCurrentLoad(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, id):
        data = []
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        cur_user = serializer.data
        recepts = Recept.objects.filter(user_id = user)
        serializer = ListReceptSerializer(recepts, many=True)
        recepts = serializer.data
        data.append(
			{
				'user': cur_user,
				'recepts': recepts
			}
        )
        return Response(data)



# информация об определенном рецепте
class ListCurrentRecept(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, id):
        print(request.user)
        dataRecept = []
        if request.user.is_authenticated:
            recept = Recept.objects.filter(pk=id)
            serializer = AuthListCurrentReceptSerializer(recept, context={'request': request}, many=True)
            dataRecept = serializer.data[:]
        else:
            recepts = Recept.objects.filter(pk=id)
            serializer = ListCurrentReceptSerializer(recepts, context={'request': request}, many=True)
            dataRecept = serializer.data[:]
            # print(dataRecept)
        recept = Gallery.objects.filter(recept=id)
        serializer = ImageReceptSerializer(recept, many=True)
        dataImage = serializer.data[:]
        # print(dataImage)
        dataRecept.append(dataImage)
        return Response(dataRecept)

# подгрузка всех комментариев к рецепту
class ListCurrentComments(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, id):


        if request.user.is_authenticated:
            comm = Comment.objects.filter(recept=id).order_by('pub_date')
            comm_data = AuthListCommentSerializer(comm, context={'request': request}, many=True)
            dataComment = comm_data.data[:]
        else:
            comm = Comment.objects.filter(recept=id).order_by('pub_date')
            comm_data = ListCommentSerializer(comm, many=True)
            dataComment = comm_data.data[:]

        return Response(dataComment)


# редактирование рецепта
class EditRecept(APIView):
    permission_classes = [permissions.IsAuthenticated,]  #for avtorise
    parser_classes = (MultiPartParser,)
    # serializer_class = AddReceptSerializer(many=True)
    # model = Recept

    def post(self, request, id):
        Recept_ID = []
        data = json.loads(request.body.decode('utf-8'))
        Text = json.loads(data['Text'])
        Comp = json.loads(data['Comp'])
        Tag = data['Tag']
        Title = data['Title']
        print(str(request.META['CONTENT_TYPE']))

        
        if ( data['Title'] != '' and data['Comp'] != '[]' and data['Text'] != '[]' and data['Tag'] != '[]'):
            Creater = User.objects.get(username=request.user)
            recept = Recept.objects.get(id=id)
            if (recept.user == Creater): 
                recept.title = Title
                recept.comp = Comp
                recept.text = Text
                recept.tag_name.clear()
                for select_tag in Tag:
                    recept.tag_name.add(select_tag['id'])
                recept.save()
                Recept_ID.append(recept.id)
                # print(type(recept.text))
                rec = Recept.objects.filter(user=Creater).count()
                obj = Profile.objects.get(user=request.user)
                obj.quantity = rec
                obj.save()
                # print(obj)
                # print("New Recept")

        return Response(Recept_ID)


# добавление рецепта
class AddRecept(APIView):
    permission_classes = [permissions.IsAuthenticated,]  #for avtorise
    parser_classes = (MultiPartParser,)
    # serializer_class = AddReceptSerializer(many=True)
    # model = Recept

    def post(self, request):
        Recept_ID = []
        data = json.loads(request.body.decode('utf-8'))
        Text = json.loads(data['Text'])
        Comp = json.loads(data['Comp'])
        Title = data['Title']
        Tag = data['Tag']
        print(str(request.META['CONTENT_TYPE']))

        
        if ( data['Title'] != '' and data['Comp'] != '[]' and data['Text'] != '[]' and data['Tag'] != []):
            Creater = User.objects.get(username=request.user)
            recept = Recept()
            recept.title = Title
            recept.comp = Comp
            recept.text = Text
            recept.user = Creater
            recept.save()
            Recept_ID.append(recept.id)
            # print(type(recept.text))
            for select_tag in Tag:
                recept.tag_name.add(select_tag['id'])
            rec = Recept.objects.filter(user=Creater).count()
            obj = Profile.objects.get(user=request.user)
            obj.quantity = rec
            obj.save()
            # print(obj)
            # print("New Recept")

        return Response(Recept_ID)
# добавление фото к рецепту
class AddReceptPhoto(APIView):
    permission_classes = [permissions.IsAuthenticated, ] #for avtorise
    def post(self, request):
        files = request.FILES.getlist('files')
        print(request.user)
        rec = Recept.objects.filter(user=request.user).order_by('-id')[0]
        if (files != []):
            print(files)
            for file in files:
                gal = Gallery()
                gal.recept = rec
                gal.image = file
                gal.save()

        return Response(status=201)

# добавление комментария к рецепту
class AddComment(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]  #for avtorise
    serializer_class = AddCommentSerializer(many=True)
    model = Comment

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if ( data['Text'] != '' and data['Recept_id'] != ''):
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

# Предполагается, что это будет функция настроек пользователя
class Me(APIView):
    permission_classes = [permissions.IsAuthenticated, ] #for avtorise
    serializer_class = UserSerializer(many=True)
    model = User

    def post(self, request):
        # print("--------------------------")
        # print(request.user)
        obj, created = Profile.objects.get_or_create(
            user=request.user, defaults={ "avatar":'media/default.png', "quantity": 0,})
        user = User.objects.get(username = request.user)
        serializer = MeUserSerializer(user, context={'request': request})
        data_user = serializer.data
        return Response(data_user)

