from rest_framework import permissions


class EhSuperUser(permissions.BasePermission):
    
    # so pode deletar se for superusuario
    def has_object_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True
            