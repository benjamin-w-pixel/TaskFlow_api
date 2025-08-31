from rest_framework import serializers
from .models import Project
from users.serializers import UserRegistrationSerializer

class ProjectSerializer(serializers.ModelSerializer):
    owner = UserRegistrationSerializer(read_only=True)
    members = UserRegistrationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'