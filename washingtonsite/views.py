import json
import logging
from uuid import UUID, uuid4

from django.conf import settings
from django.http import (
    HttpRequest,
    HttpResponseNotFound,
    HttpResponseRedirect,
    JsonResponse,
)
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods


def index(request: HttpRequest) -> TemplateResponse:
    """Render the index page."""
    return TemplateResponse(request, "washingtonsite/index.dj.html")


def calendar(request: HttpRequest) -> TemplateResponse:
    """Render the calender page."""
    return TemplateResponse(request, "washingtonsite/calendar.dj.html")


def story(request: HttpRequest) -> TemplateResponse:
    """Render the story page."""
    return TemplateResponse(request, "washingtonsite/story.dj.html")


def media(request: HttpRequest) -> TemplateResponse:
    """Render the media page."""
    return TemplateResponse(request, "washingtonsite/media.dj.html")


def links(request: HttpRequest) -> TemplateResponse:
    """Render the links page."""
    return TemplateResponse(request, "washingtonsite/links.dj.html")


def songs(request: HttpRequest) -> TemplateResponse:
    """Render the songs page."""
    return TemplateResponse(request, "washingtonsite/songs.dj.html")


def contact(request: HttpRequest) -> TemplateResponse:
    """Render the contact page."""
    return TemplateResponse(request, "washingtonsite/contact.dj.html")
