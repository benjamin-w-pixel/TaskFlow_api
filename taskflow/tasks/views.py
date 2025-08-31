from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Users can only see tasks from projects they're members of
        return Task.objects.filter(project__members=self.request.user)
    
    def perform_create(self, serializer):
        task = serializer.save()
        # Auto-assign to current user if no assignee specified
        if not task.assignee:
            task.assignee = self.request.user
            task.save()
    
    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        task = self.get_object()
        new_status = request.data.get('status')
        
        if new_status in dict(Task.STATUS_CHOICES):
            task.status = new_status
            task.save()
            return Response({'status': 'Status updated successfully'})
        return Response({'error': 'Invalid status'}, status=400)