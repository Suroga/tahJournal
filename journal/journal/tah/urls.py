from django.urls import path
from django.views.generic.base import TemplateView
from journal.tah.views import (teor, calculation1, results, downloadfile)

app_name = "tah"
urlpatterns = [
    path('teor/<int:id>', view=teor, name="teor"),
    path('calculation1/', view=calculation1, name="calculation1"),
    path('results/', view=results, name="results"),
    path('downloadfile/', view=downloadfile, name="downloadfile"),

]
