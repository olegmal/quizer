from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.is_superuser and request.user.is_authenticated:
            return True
        return False
