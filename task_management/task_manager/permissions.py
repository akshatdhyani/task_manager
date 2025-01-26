from rest_framework import permissions

class isAdmin(permissions.BasePermissions):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class isManager(permissions.BasePermissions):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'manager'
    
class isEmployee(permissions.BasePermissions):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'employee'
    
class CanManageTasks(permissions.BasePermissions):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'manager']

class CanUpdateAssignedTasks(permissions.BasePermissions):
    def has_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.role == 'employee' and obj.assigned_to == request.user