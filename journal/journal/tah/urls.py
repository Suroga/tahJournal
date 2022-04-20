from django.urls import path

from journal.tah.views import (index)

app_name = "tah"
urlpatterns = [
    path("", view=index, name="index"),
]
