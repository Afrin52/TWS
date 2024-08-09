from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from tasks.models import Task, Comment, TaskMember
from tasks.serializers import TaskSerializer, CommentSerializer, TaskMemberSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password, email=email)
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

class LoginUser(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        return Response({'token': token.key, 'user_id': user.pk, 'email': user.email})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @action(detail=True, methods=['POST'])
    def add_member(self, request, pk=None):
        task = self.get_object()
        user = User.objects.get(id=request.data['user_id'])
        TaskMember.objects.create(task=task, user=user)
        return Response({'status': 'member added'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def remove_member(self, request, pk=None):
        task = self.get_object()
        user = User.objects.get(id=request.data['user_id'])
        TaskMember.objects.filter(task=task, user=user).delete()
        return Response({'status': 'member removed'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def add_comment(self, request, pk=None):
        task = self.get_object()
        Comment.objects.create(task=task, author=request.user, text=request.data['text'])
        return Response({'status': 'comment added'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['PATCH'])
    def update_status(self, request, pk=None):
        task = self.get_object()
        task.status = request.data['status']
        task.save()
        return Response({'status': 'status updated'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def members(self, request, pk=None):
        task = self.get_object()
        members = task.members.all()
        serializer = TaskMemberSerializer(members, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def comments(self, request, pk=None):
        task = self.get_object()
        comments = task.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
