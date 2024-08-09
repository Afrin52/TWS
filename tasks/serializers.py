from rest_framework import serializers
from django.contrib.auth.models import User
from tasks.models import Task, Comment, TaskMember

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TaskMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskMember
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
