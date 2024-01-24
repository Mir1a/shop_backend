# region				-----External Imports-----
from rest_framework import routers
# endregion

# region				-----Internal Imports-----
from .frontend import views as frontend_restful
# endregion

# region			  -----Supporting Variables-----
# endregion


frontend_router = routers.DefaultRouter()

frontend_router.register(viewset=frontend_restful.UserViewSet,
                         prefix="frontend/user")