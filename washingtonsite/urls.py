from django.urls import include, path

from .views import (calendar, contact, index, links, media, song_search, songs,
                    story)

# remap:
# bkkwa.html -> index
# bkklocationswa.html -> calendar
# bkstorywa.html -> story
# bkkmediawa.html -> media
# bkklinkswa.html -> links
# bkksongswa.html -> songs
# bkkcontactwa.html -> contact

# ??? serve views twice or inline redirect ???
urlpatterns_new = [
    path("", index, name="index"),
    path("calendar", calendar, name="calendar"),
    path("story", story, name="story"),
    path("media", media, name="media"),
    path("links", links, name="links"),
    path("songs", songs, name="songs"),
    path("contact", contact, name="contact"),
    path("song-search", song_search, name="song_search"),
]

# these should probaly just be redirects
urlpatterns_old = [
    path("bkkwa.html", index, name="index-old"),
    path("bkklocationswa.html", calendar, name="calendar-old"),
    path("bkstorywa.html", story, name="story-old"),
    path("bkkmediawa.html", media, name="media-old"),
    path("bkklinkswa.html", links, name="links-old"),
    path("bkksongswa.html", songs, name="songs-old"),
    path("bkkcontactwa.html", contact, name="contact-old"),
]

urlpatterns = urlpatterns_old + [
    path("wa/", include(urlpatterns_new)),
]
