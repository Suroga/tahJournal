from django.urls import path
from django.views.generic.base import TemplateView
from journal.tah.views import (teor, calculation1, index)

app_name = "tah"
urlpatterns = [
    path('teor/<int:id>', view=teor, name="teor"),
    path('calculation1/', view=calculation1, name="calculation1"),
    path('index/', view=index, name="index"),

]
