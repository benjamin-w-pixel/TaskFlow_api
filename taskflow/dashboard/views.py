from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from tasks.models import Task
from projects.models import Project

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_overview(request):
    user = request.user
    
    
    user_projects = Project.objects.filter(members=user)
    total_projects = user_projects.count()
    
    
    user_tasks = Task.objects.filter(project__in=user_projects)
    total_tasks = user_tasks.count()
    completed_tasks = user_tasks.filter(status='DONE').count()
    
    
    if total_tasks > 0:
        completion_rate = round((completed_tasks / total_tasks) * 100, 2)
    else:
        completion_rate = 0.0
    
    return Response({
        'total_projects': total_projects,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'completion_rate': completion_rate,
        'user': user.username
    })
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def upcoming_tasks(request):
    user = request.user
    seven_days_later = timezone.now() + timedelta(days=7)
    
    upcoming = Task.objects.filter(
        project__members=user,
        deadline__gte=timezone.now(),
        deadline__lte=seven_days_later,
        status__in=['TODO', 'IN_PROGRESS']
    ).order_by('deadline')[:10]
    
    from tasks.serializers import TaskSerializer
    return Response(TaskSerializer(upcoming, many=True).data)