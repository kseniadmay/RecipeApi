from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Разрешение на редактирование доступно только автору, чтение доступно всем"""

    def has_object_permission(self, request, view, obj):
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Редактирование только автору
        return obj.author == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    """Разрешение на создание и редактирование только администраторам, чтение доступно всем"""

    def has_permission(self, request, view):
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Создание и редактирование только администратору
        return request.user and request.user.is_staff