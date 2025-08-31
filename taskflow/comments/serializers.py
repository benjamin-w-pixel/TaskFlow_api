from rest_framework import serializers
from .models import Comment
from users.serializers import UserRegistrationSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = UserRegistrationSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'