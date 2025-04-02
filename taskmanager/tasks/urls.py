from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, CommentViewSet, TaskHistoryViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'task-history', TaskHistoryViewSet, basename='taskhistory')  # Optional basename

urlpatterns = [
    path('', include(router.urls)),
]
