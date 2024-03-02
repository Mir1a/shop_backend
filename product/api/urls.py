# region				-----External Imports-----
from rest_framework import routers
# endregion

# region				-----Internal Imports-----
from .frontend import views as frontend_restful
# endregion

# region			  -----Supporting Variables-----
# endregion


frontend_router = routers.DefaultRouter()

frontend_router.register(viewset=frontend_restful.ItemViewSet,
                         prefix="frontend/item")
frontend_router.register(viewset=frontend_restful.OrderViewSet,
                         prefix="frontend/order")
frontend_router.register(viewset=frontend_restful.Supply_senderViewSet,
                         prefix="frontend/supply_sender")