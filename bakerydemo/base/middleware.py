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
