from rest_framework import permissions


class AuthPermission(permissions.BasePermission):
    """
    Проверка аутентификации пользователя.
    """
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class FollowPermission(permissions.BasePermission):
    """
    Проверка аутентификации пользователя.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # def has_object_permission(self, request, view, obj):
    #     return (
    #         request.method in permissions.SAFE_METHODS
    #         or obj.author != request.user
    #     )
