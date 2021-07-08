from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework import generics, viewsets, permissions, views
from rest_framework.response import Response

from .models import Profile, Registro
from .serializers import ProfileSerializer, RegistroSerializer, UserSerializer, GroupSerializer
from .permissions import DjangoModelPermissionWithGET


class HelloView(views.APIView):
    #permission_classes = [permissions.a]
    queryset = User.objects.none()

    def get(self, request):
        content = {
            'ok': True,
            'url': 'https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4'
        }
        return Response(content)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [DjangoModelPermissionWithGET]


class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [DjangoModelPermissionWithGET]


class UserDataView(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
