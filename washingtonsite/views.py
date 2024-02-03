import json
from logging import getLogger
from uuid import UUID, uuid4

from django.conf import settings
from django.http import (HttpRequest, HttpResponseNotFound,
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from requests import get as http_get

log = getLogger(__name__)


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


def song_search(request: HttpRequest) -> TemplateResponse:
    """proxy shep's song search"""

    base_url = "https://bkk.schepman.org/jsonp?search="

    try:
        query = request.GET.get("search", "")
        filter = request.GET.get("searchBy", "artist")

        log.info(f"searching for {query} by {filter}")

        if not query:
            return JsonResponse({"error": "no query"})

        result = http_get(f"{base_url}{query}&searchby={filter}")

        if result.ok:
            # TODO: just proxy the data (?or cache here? with short limit)
            # TODO: paginate resp ???
            data = result.json()
            log.info(f"got {len(data)} results")
            return JsonResponse({'data':data}, safe=False)
        else:
            print("ERR", result)
            return JsonResponse({"error": "no results"})

    except Exception as e:
        log.exception(e)
    return HttpResponseNotFound()
