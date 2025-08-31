from rest_framework import viewsets, permissions
from .models import Comment
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Users can only see comments from tasks they have access to
        return Comment.objects.filter(task__project__members=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)