import json
import logging
from uuid import UUID, uuid4

from django.conf import settings
from django.http import (HttpRequest, HttpResponseNotFound,
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods


def index(request: HttpRequest) -> TemplateResponse:
    """Render the index page."""
    return TemplateResponse(request, "website/index.dj.html")
def menus(request: HttpRequest) -> TemplateResponse:
    """Render the index page."""
    return TemplateResponse(request, "website/menus.dj.html")


# this should go up
def splash(request: HttpRequest) -> TemplateResponse:
    """Render the splash page."""
    return TemplateResponse(request, "website/splash.dj.html")
