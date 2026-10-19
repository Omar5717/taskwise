from django.shortcuts import render
from task_app.serializers import UserSerializer,TaskSerializer
from task_app.models import Task
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class SignupViewSet(ViewSet):
    def create(self,request):
        dser=UserSerializer(data=request.data)
        if dser.is_valid():
            User.objects.create_user(**dser.validated_data)
            return Response(data=dser.data,status=status.HTTP_201_CREATED)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(ModelViewSet):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=TaskSerializer
    queryset=Task.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def  get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    

