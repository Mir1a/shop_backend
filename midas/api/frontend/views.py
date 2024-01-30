# region				-----External Imports-----
from rest_framework import viewsets, mixins as rest_mixins, renderers, permissions as rest_permissions
from django import shortcuts
from utils import mixins as utils_mixins
# endregion

# region				-----Internal Imports-----
from ...models import User
from . import permissions
from . import serializers
# endregion


class UserViewSet(utils_mixins.DynamicSerializersViewSet,
                  utils_mixins.PrefetchableRetrieveMixin,
                  rest_mixins.CreateModelMixin,
                  rest_mixins.UpdateModelMixin,
                  rest_mixins.DestroyModelMixin):
    # region		   -----Dynamic Serializers-----
    default_serializer_class = serializers.ReadUserSerializer
    serializer_classes = {"create": serializers.RegisterUserSerializer,
                          "partial_update": serializers.WriteUserSerializer}
    # endregion

    # region		   -----Default Parameters-----
    queryset = User.objects
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [permissions.CreateOrIsAuthenticated]
    # endregion

    # region		   -----Prefetch Functions-----
    def _prefetch_retrieve(self, queryset):
        return queryset\
            .prefetch_related("favorites")\
            .only('id', 'name', 'email', 'last_name',
                  'avatar', 'born')
    # endregion

    # region		    -----Default Function-----
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = shortcuts.get_object_or_404(queryset, pk=self.request.user.pk)
        self.check_object_permissions(self.request, obj)
        return obj
    # endregion
