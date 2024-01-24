from rest_framework import viewsets, mixins, renderers, permissions as rest_permissions
from django import shortcuts
from ..general import serializers
from ...models import User
from . import permissions


class UserViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [permissions.CreateOrIsAuthenticated]

    # region		    -----Default Function-----
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = shortcuts.get_object_or_404(queryset, pk=self.request.user.pk)
        self.check_object_permissions(self.request, obj)
        return obj
    # endregion
