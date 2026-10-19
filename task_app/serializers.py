from rest_framework import serializers
from task_app.models import Task

class UserSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"
        read_only_fields=["created_at","owner"]

