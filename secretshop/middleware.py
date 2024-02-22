# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _

from django import http as django_http
import traceback
from typing import Dict, Callable
import logging
# endregion

# region			  -----Supporting Variables-----
from utils.exception import ExtendedValidationError

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


class Process4XXError(object):
    def __init__(self, get_response: Callable) -> None:
        self._get_response = get_response

    def __call__(self, request: Dict) -> Dict:
        response = self._get_response(request)

        return response

    def process_exception(self, request: Dict,
        exception: Exception)\
            -> django_http.JsonResponse:
        if isinstance(exception, ExtendedValidationError):
            return django_http.JsonResponse({"detail": exception.detail}, status=exception.status_code)