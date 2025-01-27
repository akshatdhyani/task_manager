from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.hashers import make_password
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list', 'update_role']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
    
    @action(detail=True, methods=['put'], url_path='role')
    def update_role(self, request, pk=None):
        user = self.get_object()
        user.role = request.data.get('role')
        user.save()
        return Response({'message': 'Role has been updated.'})
    
    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        print("Request Data:", request.data)
        data = request.data
        required_fields = ['username', 'email', 'password', 'role']

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return Response(
                {"error": f"Missing fields:{', '.join(missing_fields)}"},
                status= status.HTTP_400_BAD_REQUEST
            ) 
        
        if data['role'] not in ['admin', 'manager', 'employee']:
            return Response(
                {"error": "Invalid role. Role should be either 'admin' or 'manager' or 'employee'"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if User.objects.filter(username=data['username']).exists():
            return Response({"error": "Username is already in use"})
        
        user = User(
            username = data['username'],
            email = data['email'],
            password=make_password(data['password']),
            role = data['role']
        )
        user.save()
        return Response({'message': 'User has been registered. Thankyou for registering'}, status=status.HTTP_201_CREATED)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.action in ['create', 'assign']:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated()]
    
    @action(detail=True, methods=['post'], url_path='assign')
    def assign_task(self, request, pk=None):
        task = self.get_object()
        employee_id = request.data.get('assigned_to')
        employee = User.objects.filter(id=employee_id, role='employee').first()
        if employee:
            task.assigned_to = employee
            task.save()
            return Response({'message': 'Task has been assigned to the employee.'})
        return Response({'error': 'Invalid employee ID. Please enter a valid employee ID.'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['delete'], url_path='delete')
    def delete_task(self, request, pk=None):
        task = self.get_object()
        task.delete()
        return Response({'message': 'Task Deleted.'})
    
