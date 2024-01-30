from django.urls import path

from .views import calendar, contact, index, links, media, songs, story

# remap:
# bkkwa.html -> index
# bkklocationswa.html -> calendar
# bkstorywa.html -> story
# bkkmediawa.html -> media
# bkklinkswa.html -> links
# bkksongswa.html -> songs
# bkkcontactwa.html -> contact

# ??? serve views twice or inline redirect ???
urlpatterns = [
    path("", index, name="index"),
    path("bkkwa.html", index, name="index-old"),
    path("calendar", calendar, name="calendar"),
    path("bkklocationswa.html", calendar, name="calendar-old"),
    path("story", story, name="story"),
    path("bkstorywa.html", story, name="story-old"),
    path("media", media, name="media"),
    path("bkkmediawa.html", media, name="media-old"),
    path("links", links, name="links"),
    path("bkklinkswa.html", links, name="links-old"),
    path("songs", songs, name="songs"),
    path("bkksongswa.html", songs, name="songs-old"),
    path("contact", contact, name="contact"),
    path("bkkcontactwa.html", contact, name="contact-old"),
]
