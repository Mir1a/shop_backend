# region				-----External Imports-----
from rest_framework import permissions
import typing
# endregion


class CreateOrIsAuthenticated(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return (view.action == 'create'
                or super(CreateOrIsAuthenticated, self)
                .has_permission(request, view))
