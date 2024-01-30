# region				-----External Imports-----
from rest_framework import permissions
import typing
# endregion


class IsAuthenticated(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return (view.action == 'create'
                or super(IsAuthenticated, self)
                .has_permission(request, view))