import pytz
from django.urls import reverse
from django.utils import timezone


class NoIndexMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Set no index on all paths
        response["X-Robots-Tag"] = "noindex"

        return response

class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Allow cross origin requests on all paths
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        response["Access-Control-Allow-Methods"] = "*"

        return response
