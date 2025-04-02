from django.db.models import Q  # Importing Q for complex queries
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task, Project, Comment, TaskHistory
from .serializers import (
    TaskSerializer, TaskCreateUpdateSerializer,
    ProjectSerializer, CommentSerializer,
    CommentCreateSerializer, TaskHistorySerializer
)
from .permissions import IsTaskCreatorOrAssignee, IsCommentAuthor

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'description']

    def get_queryset(self):
        return self.queryset.filter(members=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated, IsTaskCreatorOrAssignee]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'priority', 'project', 'created_by']
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'created_at', 'priority']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TaskCreateUpdateSerializer
        return TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(
            Q(created_by=user) | 
            Q(assigned_to=user) |
            Q(project__members=user)
        ).distinct()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsCommentAuthor]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CommentCreateSerializer
        return CommentSerializer

    def get_queryset(self):
        task_id = self.request.query_params.get('task_id')
        if task_id:
            return self.queryset.filter(task_id=task_id)
        return self.queryset.all()  # If no task_id is provided, return all comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class TaskHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TaskHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        task_id = self.request.query_params.get('task_id')
        if task_id:
            return TaskHistory.objects.filter(task_id=task_id)
        return TaskHistory.objects.none()
