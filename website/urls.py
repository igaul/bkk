from django.urls import include, path

from washingtonsite.urls import urlpatterns_new as washingtonsite_urls
from washingtonsite.urls import urlpatterns_old as washingtonsite_old_urls
from website.views import index, menus, splash

# TODO: move this to project/urls.py


oregon_urls = [path("", index, name="index"),path("menus", menus, name="menus")]

urlpatterns = [
    path("", splash, name="splash"),
    # for old links TODO: redirect map to new urls
    path("", include(washingtonsite_old_urls)),  # , namespace="washingtonsite-old"
    path("or/", include((oregon_urls, "website"), namespace="website")),
    path(
        "wa/",
        include((washingtonsite_urls, "washingtonsite"), namespace="washingtonsite"),
    ),
]
