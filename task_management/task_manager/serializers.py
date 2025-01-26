from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'role']
    
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.StringRelatedField()
    assigned_by = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = '__all__'