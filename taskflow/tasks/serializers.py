from rest_framework import serializers
from .models import Task
from users.serializers import UserRegistrationSerializer
from projects.serializers import ProjectSerializer

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'