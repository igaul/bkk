from django.urls import include, path

from washingtonsite.urls import urlpatterns_new as washingtonsite_urls
from washingtonsite.urls import urlpatterns_old as washingtonsite_old_urls
from website.views import index, splash

# TODO: move this to project/urls.py


oregon_urls = [path("", index, name="index")]

urlpatterns = [
    path("", splash, name="splash"),
    # for old links TODO: redirect map to new urls
    path("", include(washingtonsite_old_urls)),
    path("or/", include(oregon_urls)),
    path("wa/", include(washingtonsite_urls)),
]
