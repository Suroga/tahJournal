from django.urls import path
from django.views.generic.base import TemplateView
from journal.tah.views import (index, teor1)

app_name = "tah"
urlpatterns = [
    path("блаблабла/", view=index, name="index"),
    path('teor1/',view=teor1, name="teor1"),
]
