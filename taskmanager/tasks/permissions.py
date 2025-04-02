from rest_framework.permissions import BasePermission

class IsTaskCreatorOrAssignee(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.created_by == request.user or request.user in obj.assigned_to.all()

class IsCommentAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user