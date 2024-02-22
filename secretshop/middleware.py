# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _

from django import http as django_http
import traceback
from typing import Dict, Callable
import logging
# endregion

# region			  -----Supporting Variables-----
logger = logging.getLogger(__file__)
# endregion


class Process500Error(object):
    def __init__(self, get_response: Callable) -> None:
        self._get_response = get_response
    
    def __call__(self, request: Dict) -> Dict:
        return self._get_response(request)
    
    def process_exception(self, request: Dict, 
        exception: Exception)\
            -> django_http.JsonResponse:

        logger.error(traceback.format_exc())
        return django_http.JsonResponse({
            "detail": _("Something went wrong"),
            "traceback": traceback.format_exc().split("\n"),
            "success": False
        }, status=500)

