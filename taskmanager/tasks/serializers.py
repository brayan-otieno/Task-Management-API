# tasks/serializers.py
from rest_framework import serializers
from .models import Task, Project

class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    subtasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
